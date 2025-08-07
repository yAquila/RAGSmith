"""
FastAPI interface for the genetic algorithm component combination search.

This module provides a REST API interface for external projects to interact
with the genetic algorithm system for finding optimal component combinations.
"""

import asyncio
import logging
import time
import traceback
from typing import List, Dict, Any, Optional, Callable
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import uvicorn

# Import genetic algorithm components
from genetic_algorithm import GeneticAlgorithm, GenerationStatistics
from config import GAConfig
from selection import TournamentSelection, RouletteWheelSelection, RankSelection
from crossover import SinglePointCrossover, UniformCrossover, MultiPointCrossover
from mutation import RandomMutation, AdaptiveMutation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global storage for running jobs
running_jobs: Dict[str, Dict[str, Any]] = {}


class CategorySizes(BaseModel):
    """Model for category sizes configuration."""
    sizes: List[int] = Field(..., description="Number of boxes in each category", min_items=1)
    
    @validator('sizes')
    def validate_sizes(cls, v):
        if any(size < 1 for size in v):
            raise ValueError("All category sizes must be at least 1")
        return v


class GAConfigRequest(BaseModel):
    """Model for genetic algorithm configuration request."""
    category_sizes: List[int] = Field(..., description="Number of boxes in each category")
    population_size: int = Field(50, ge=2, le=1000, description="Population size")
    generations: int = Field(100, ge=1, le=10000, description="Maximum generations")
    crossover_rate: float = Field(0.8, ge=0.0, le=1.0, description="Crossover probability")
    mutation_rate: float = Field(0.1, ge=0.0, le=1.0, description="Mutation probability")
    elitism_count: int = Field(2, ge=0, description="Number of elite individuals to preserve")
    
    # Selection method
    selection_method: str = Field("tournament", description="Selection method: tournament, roulette, rank")
    tournament_size: int = Field(3, ge=2, description="Tournament size for tournament selection")
    
    # Crossover method
    crossover_method: str = Field("single_point", description="Crossover method: single_point, uniform, multi_point")
    crossover_points: int = Field(2, ge=1, description="Number of points for multi-point crossover")
    uniform_probability: float = Field(0.5, ge=0.0, le=1.0, description="Probability for uniform crossover")
    
    # Mutation method
    mutation_method: str = Field("random", description="Mutation method: random, adaptive")
    adaptive_min_rate: float = Field(0.01, ge=0.0, le=1.0, description="Minimum rate for adaptive mutation")
    adaptive_max_rate: float = Field(0.5, ge=0.0, le=1.0, description="Maximum rate for adaptive mutation")
    
    # Termination criteria
    convergence_threshold: int = Field(20, ge=1, description="Generations without improvement before stopping")
    target_fitness: Optional[float] = Field(None, ge=0.0, le=100.0, description="Target fitness to reach")
    
    # Runtime settings
    random_seed: Optional[int] = Field(None, description="Random seed for reproducibility")
    verbose: bool = Field(False, description="Enable verbose output")


class EvaluationFunction(BaseModel):
    """Model for evaluation function specification."""
    function_type: str = Field(..., description="Type of evaluation function")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Function parameters")


class OptimizationRequest(BaseModel):
    """Model for optimization request."""
    job_id: str = Field(..., description="Unique job identifier")
    config: GAConfigRequest = Field(..., description="Genetic algorithm configuration")
    evaluation_function: EvaluationFunction = Field(..., description="Evaluation function specification")
    async_execution: bool = Field(True, description="Whether to run asynchronously")


class OptimizationResult(BaseModel):
    """Model for optimization results."""
    job_id: str
    status: str  # "running", "completed", "failed"
    best_combination: Optional[List[int]] = None
    best_fitness: Optional[float] = None
    generations_completed: Optional[int] = None
    total_time: Optional[float] = None
    converged: Optional[bool] = None
    target_reached: Optional[bool] = None
    error_message: Optional[str] = None
    statistics: Optional[List[Dict[str, Any]]] = None


class JobStatus(BaseModel):
    """Model for job status response."""
    job_id: str
    status: str
    progress: Optional[float] = None  # 0.0 to 1.0
    current_generation: Optional[int] = None
    best_fitness: Optional[float] = None
    estimated_time_remaining: Optional[float] = None


# Evaluation function registry
def create_evaluation_function(func_spec: EvaluationFunction) -> Callable[[List[int]], float]:
    """Create evaluation function based on specification."""
    
    if func_spec.function_type == "simple_sum":
        def evaluate(candidate: List[int]) -> float:
            """Simple sum evaluation with optional scaling."""
            scale = func_spec.parameters.get("scale", 2.0)
            max_value = func_spec.parameters.get("max_value", 100.0)
            return min(max_value, sum(candidate) * scale)
        return evaluate
    
    elif func_spec.function_type == "weighted_sum":
        def evaluate(candidate: List[int]) -> float:
            """Weighted sum evaluation."""
            weights = func_spec.parameters.get("weights", [1.0] * len(candidate))
            if len(weights) != len(candidate):
                weights = [1.0] * len(candidate)
            
            score = sum(gene * weight for gene, weight in zip(candidate, weights))
            return min(100.0, max(0.0, score))
        return evaluate
    
    elif func_spec.function_type == "polynomial":
        def evaluate(candidate: List[int]) -> float:
            """Polynomial evaluation function."""
            coefficients = func_spec.parameters.get("coefficients", [1.0, 0.1, 0.01])
            
            score = 0.0
            for i, gene in enumerate(candidate):
                for j, coeff in enumerate(coefficients):
                    score += coeff * (gene ** (j + 1))
            
            # Add interaction terms
            interaction_weight = func_spec.parameters.get("interaction_weight", 0.1)
            for i in range(len(candidate) - 1):
                score += interaction_weight * candidate[i] * candidate[i + 1]
            
            return min(100.0, max(0.0, score))
        return evaluate
    
    elif func_spec.function_type == "external_rag_api":
        def evaluate(candidate: List[int]) -> float:
            """External RAG API evaluation function."""
            from rag_evaluator import RAGPipelineEvaluator
            
            # Get API configuration from parameters
            api_endpoint = func_spec.parameters.get("api_endpoint", "http://example.com/api/evaluate")
            timeout = func_spec.parameters.get("timeout", 300)
            max_retries = func_spec.parameters.get("max_retries", 3)
            
            # Create evaluator instance
            evaluator = RAGPipelineEvaluator(
                api_endpoint=api_endpoint,
                timeout=timeout,
                max_retries=max_retries
            )
            
            # Evaluate the candidate
            return evaluator.evaluate(candidate)
        return evaluate
    
    elif func_spec.function_type == "custom_rag":
        def evaluate(candidate: List[int]) -> float:
            """RAG pipeline evaluation function."""
            if len(candidate) < 5:
                return 0.0
            
            # Component scores based on predefined lookup tables
            component_scores = func_spec.parameters.get("component_scores", {})
            
            # Default scoring if not provided
            default_scores = [
                [10, 25, 30, 35, 20],  # Embedding models
                [15, 25, 20],          # Vector databases
                [12, 18, 22, 28, 15, 20],  # Retrieval strategies
                [20, 35, 30, 40, 25, 45, 35],  # LLM models
                [10, 20, 25]           # Prompt templates
            ]
            
            total_score = 0.0
            for i, gene in enumerate(candidate[:5]):
                scores = component_scores.get(f"component_{i}", default_scores[i] if i < len(default_scores) else [10, 20, 30])
                if gene < len(scores):
                    total_score += scores[gene]
                else:
                    total_score += scores[-1]  # Use last score if gene is out of range
            
            # Synergy bonuses
            synergy_bonus = 0.0
            if len(candidate) >= 5:
                if candidate[0] >= 2 and candidate[3] >= 4:  # Good embedding + good LLM
                    synergy_bonus += 15.0
                if candidate[1] == 1 and candidate[2] in [2, 3]:  # Good DB + retrieval
                    synergy_bonus += 10.0
            
            final_score = total_score + synergy_bonus
            return min(100.0, max(0.0, (final_score / 200.0) * 100.0))
        return evaluate
    
    else:
        raise ValueError(f"Unknown evaluation function type: {func_spec.function_type}")


def create_ga_config(config_req: GAConfigRequest) -> GAConfig:
    """Create GAConfig from request model."""
    
    # Create selection method
    if config_req.selection_method == "tournament":
        selection_method = TournamentSelection(tournament_size=config_req.tournament_size)
    elif config_req.selection_method == "roulette":
        selection_method = RouletteWheelSelection()
    elif config_req.selection_method == "rank":
        selection_method = RankSelection()
    else:
        raise ValueError(f"Unknown selection method: {config_req.selection_method}")
    
    # Create crossover method
    if config_req.crossover_method == "single_point":
        crossover_method = SinglePointCrossover()
    elif config_req.crossover_method == "uniform":
        crossover_method = UniformCrossover(probability=config_req.uniform_probability)
    elif config_req.crossover_method == "multi_point":
        crossover_method = MultiPointCrossover(num_points=config_req.crossover_points)
    else:
        raise ValueError(f"Unknown crossover method: {config_req.crossover_method}")
    
    # Create mutation method
    if config_req.mutation_method == "random":
        mutation_method = RandomMutation(mutation_rate=config_req.mutation_rate)
    elif config_req.mutation_method == "adaptive":
        mutation_method = AdaptiveMutation(
            base_mutation_rate=config_req.mutation_rate,
            min_mutation_rate=config_req.adaptive_min_rate,
            max_mutation_rate=config_req.adaptive_max_rate
        )
    else:
        raise ValueError(f"Unknown mutation method: {config_req.mutation_method}")
    
    # Create GAConfig
    return GAConfig(
        category_sizes=config_req.category_sizes,
        population_size=config_req.population_size,
        generations=config_req.generations,
        crossover_rate=config_req.crossover_rate,
        mutation_rate=config_req.mutation_rate,
        elitism_count=config_req.elitism_count,
        selection_method=selection_method,
        crossover_method=crossover_method,
        mutation_method=mutation_method,
        convergence_threshold=config_req.convergence_threshold,
        target_fitness=config_req.target_fitness,
        random_seed=config_req.random_seed,
        verbose=config_req.verbose
    )


async def run_optimization_async(job_id: str, config: GAConfig, evaluate_func: Callable) -> None:
    """Run genetic algorithm optimization asynchronously."""
    try:
        logger.info(f"Starting optimization job {job_id}")
        
        # Update job status
        running_jobs[job_id]["status"] = "running"
        running_jobs[job_id]["start_time"] = time.time()
        
        # Create and run genetic algorithm
        ga = GeneticAlgorithm(config, evaluate_func)
        
        # Run optimization
        results = ga.run()
        
        # Convert statistics to serializable format
        statistics = []
        if results.get("statistics"):
            for stat in results["statistics"]:
                statistics.append({
                    "generation": stat.generation,
                    "best_fitness": stat.best_fitness,
                    "worst_fitness": stat.worst_fitness,
                    "average_fitness": stat.average_fitness,
                    "diversity_score": stat.diversity_score,
                    "best_individual_genes": stat.best_individual_genes,
                    "execution_time": stat.execution_time
                })
        
        # Update job with results
        running_jobs[job_id].update({
            "status": "completed",
            "results": {
                "best_combination": results["best_combination"],
                "best_fitness": results["best_fitness"],
                "generations_completed": results["generations_completed"],
                "total_time": results["total_time"],
                "converged": results["converged"],
                "target_reached": results["target_reached"],
                "statistics": statistics
            },
            "end_time": time.time()
        })
        
        logger.info(f"Completed optimization job {job_id}")
        
    except Exception as e:
        logger.error(f"Error in optimization job {job_id}: {str(e)}")
        logger.error(traceback.format_exc())
        
        running_jobs[job_id].update({
            "status": "failed",
            "error": str(e),
            "end_time": time.time()
        })


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for FastAPI app."""
    logger.info("Starting Genetic Algorithm API server")
    yield
    logger.info("Shutting down Genetic Algorithm API server")


# Create FastAPI app
app = FastAPI(
    title="Genetic Algorithm Component Search API",
    description="REST API for genetic algorithm-based component combination optimization",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Genetic Algorithm Component Search API",
        "version": "1.0.0",
        "description": "REST API for optimizing component combinations using genetic algorithms",
        "endpoints": {
            "POST /optimize": "Start optimization job",
            "GET /status/{job_id}": "Get job status",
            "GET /result/{job_id}": "Get job results",
            "GET /jobs": "List all jobs",
            "DELETE /job/{job_id}": "Cancel/delete job",
            "GET /health": "Health check"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "active_jobs": len([job for job in running_jobs.values() if job["status"] == "running"])
    }


@app.post("/optimize", response_model=OptimizationResult)
async def start_optimization(request: OptimizationRequest, background_tasks: BackgroundTasks):
    """Start genetic algorithm optimization."""
    
    job_id = request.job_id
    
    # Check if job already exists
    if job_id in running_jobs:
        raise HTTPException(status_code=400, detail=f"Job {job_id} already exists")
    
    try:
        # Create GA configuration
        config = create_ga_config(request.config)
        
        # Create evaluation function
        evaluate_func = create_evaluation_function(request.evaluation_function)
        
        # Initialize job tracking
        running_jobs[job_id] = {
            "status": "initializing",
            "config": request.config.dict(),
            "evaluation_function": request.evaluation_function.dict(),
            "created_time": time.time()
        }
        
        if request.async_execution:
            # Run asynchronously
            background_tasks.add_task(run_optimization_async, job_id, config, evaluate_func)
            
            return OptimizationResult(
                job_id=job_id,
                status="running"
            )
        else:
            # Run synchronously
            logger.info(f"Starting synchronous optimization job {job_id}")
            
            ga = GeneticAlgorithm(config, evaluate_func)
            results = ga.run()
            
            # Convert statistics
            statistics = []
            if results.get("statistics"):
                for stat in results["statistics"]:
                    statistics.append({
                        "generation": stat.generation,
                        "best_fitness": stat.best_fitness,
                        "worst_fitness": stat.worst_fitness,
                        "average_fitness": stat.average_fitness,
                        "diversity_score": stat.diversity_score,
                        "best_individual_genes": stat.best_individual_genes,
                        "execution_time": stat.execution_time
                    })
            
            # Store results
            running_jobs[job_id].update({
                "status": "completed",
                "results": results,
                "end_time": time.time()
            })
            
            return OptimizationResult(
                job_id=job_id,
                status="completed",
                best_combination=results["best_combination"],
                best_fitness=results["best_fitness"],
                generations_completed=results["generations_completed"],
                total_time=results["total_time"],
                converged=results["converged"],
                target_reached=results["target_reached"],
                statistics=statistics
            )
            
    except Exception as e:
        logger.error(f"Error starting optimization job {job_id}: {str(e)}")
        
        # Clean up failed job
        if job_id in running_jobs:
            running_jobs[job_id].update({
                "status": "failed",
                "error": str(e)
            })
        
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/status/{job_id}", response_model=JobStatus)
async def get_job_status(job_id: str):
    """Get status of optimization job."""
    
    if job_id not in running_jobs:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    
    job = running_jobs[job_id]
    
    # Calculate progress if running
    progress = None
    current_generation = None
    best_fitness = None
    estimated_time_remaining = None
    
    if job["status"] == "running" and "results" in job:
        # This would be updated by the running algorithm
        # For now, we'll provide basic status
        pass
    
    return JobStatus(
        job_id=job_id,
        status=job["status"],
        progress=progress,
        current_generation=current_generation,
        best_fitness=best_fitness,
        estimated_time_remaining=estimated_time_remaining
    )


@app.get("/result/{job_id}", response_model=OptimizationResult)
async def get_job_result(job_id: str):
    """Get results of optimization job."""
    
    if job_id not in running_jobs:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    
    job = running_jobs[job_id]
    
    if job["status"] == "running":
        return OptimizationResult(job_id=job_id, status="running")
    elif job["status"] == "failed":
        return OptimizationResult(
            job_id=job_id,
            status="failed",
            error_message=job.get("error", "Unknown error")
        )
    elif job["status"] == "completed":
        results = job["results"]
        return OptimizationResult(
            job_id=job_id,
            status="completed",
            best_combination=results["best_combination"],
            best_fitness=results["best_fitness"],
            generations_completed=results["generations_completed"],
            total_time=results["total_time"],
            converged=results["converged"],
            target_reached=results["target_reached"],
            statistics=results.get("statistics")
        )
    else:
        return OptimizationResult(job_id=job_id, status=job["status"])


@app.get("/jobs")
async def list_jobs():
    """List all jobs with their statuses."""
    
    jobs_summary = []
    for job_id, job in running_jobs.items():
        jobs_summary.append({
            "job_id": job_id,
            "status": job["status"],
            "created_time": job.get("created_time"),
            "start_time": job.get("start_time"),
            "end_time": job.get("end_time"),
            "best_fitness": job.get("results", {}).get("best_fitness") if job["status"] == "completed" else None
        })
    
    return {"jobs": jobs_summary, "total_jobs": len(jobs_summary)}


@app.delete("/job/{job_id}")
async def delete_job(job_id: str):
    """Cancel or delete a job."""
    
    if job_id not in running_jobs:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    
    job = running_jobs[job_id]
    
    # Note: For a production system, you'd want to implement proper job cancellation
    # This would require thread/process management
    
    if job["status"] == "running":
        # Mark as cancelled (in a real implementation, you'd stop the actual process)
        job["status"] = "cancelled"
        job["end_time"] = time.time()
        return {"message": f"Job {job_id} marked for cancellation"}
    else:
        # Remove completed/failed jobs
        del running_jobs[job_id]
        return {"message": f"Job {job_id} deleted"}


if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    ) 