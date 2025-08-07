PRE_EMBEDDING_PROMPTS = {
    "cch_semantic": """Generate a concise header (3-5 words) that captures the main topic of this document section. 
The header should be descriptive and help with information retrieval.

Document content:
{content}

Header:""",
    "cch_query_aware": """Generate a header that would help answer questions about this content. 
The header should be relevant for search and retrieval purposes.

Document content:
{content}

Header:""",
    "cch_structural": """Extract or generate a section title for this content. 
If the content has a clear title or heading, use it. Otherwise, generate a descriptive title.

Document content:
{content}

Title:""",

    "hype": """Analyze the input text and generate {num_hype_questions} essential questions that, when answered, capture the main points of the text. 
Each question should be one line, without numbering or prefixes.

Input Text:
{document}

{num_hype_questions} Essential Questions:"""
}

QUERY_EXPANSION_PROMPTS = {
    "simple_multi_query": """
You are an efficient Query Expander. Your task is to read the query provided below and expand it into only {num_expanded_queries} variations.

### Output Format
You must output the expanded queries in the following format:
1. ...
2. ...
...
...
{num_expanded_queries}. ...

### Query to Expand
{query}

### Expanded Queries
    """,

    "hyde": """Imagine you are an expert writing a detailed explanation on the topic: '{query}'
Your responses should be comprehensive and include all key points that would be found in the top search result. You should output ONLY {num_expanded_queries} documents in the following format:

Document 1:
...
Document {num_expanded_queries}:
...

Do not add any other text.
    """,

    "decomposition": """
Your task is to rewrite a user's query into {num_expanded_queries} more specific queries. Your output must be ONLY a numbered list of the new queries. Do not add any other text.

---
Example:
User Query: "benefits of intermittent fasting"
Number of Queries: 3
New Queries:
1. What are the weight loss results of intermittent fasting?
2. Risks and side effects of intermittent fasting.
3. How does intermittent fasting affect metabolic health?
---

Now, do this for the following query.

User Query: "{query}"
Number of Queries: {num_expanded_queries}
New Queries:
    """,

    "step_back_prompting": """
    You are an expert at answering all kind of Questions. Your task is to step back and paraphrase a question to at most {num_expanded_queries} more generic step-back questions, which is easier to answer. Here are a few examples:
    "input": "Could the members of The Police perform lawful arrests?",
    "output": "what can the members of The Police do?"
    "input": "Jan Sindel's was born in what country?",
    "output": "what is Jan Sindel's personal history?"

    Now, do this for the following query and output at most {num_expanded_queries} step-back questions in the following format:
    1. ...
    2. ...
    ...
    {num_expanded_queries}. ...

    User Query: "{query}"
    1. 
    """,

    "refinement_clarification": """
You are an expert at improving search queries. Your task is to rewrite the given query to make it more search-friendly and clear.

### Guidelines:
- Keep the original intent
- Make it more specific if needed
- Use clear, searchable terms
- Maintain the same meaning
- Output ONLY the improved query, nothing else

### Original Query:
{query}

### Improved Query:
    """,

    "refinement_rephrasing": """
You are an expert at rephrasing queries to make them clearer and more search-friendly.

### Task:
Rephrase the following query in a clearer, more specific way while maintaining the original intent.

### Guidelines:
- Keep the same meaning and intent
- Make it more specific and clear
- Use proper grammar and structure
- Output ONLY the rephrased query, nothing else

### Original Query:
{query}

### Rephrased Query:
    """,
    "refinement_keyword_extraction": """
You are an expert at extracting key search terms from queries.

### Task:
Extract the most important keywords and phrases from the given query that would be useful for search.

### Guidelines:
- Focus on the main concepts and entities
- Include synonyms if relevant
- Keep terms in a searchable format
- Output ONLY the key terms separated by spaces, nothing else

### Original Query:
{query}

### Key Terms:
    """
}

PASSAGE_RERANKING_PROMPTS = {
    "llm_rerank": """
    Rank these passages by relevance to the query: {query}\n\nPassages:\n{passages}\n\nRanked Passages:
    """
}

PASSAGE_COMPRESS_PROMPTS = {
    "tree_summarize_prompt": """
Write a summary of the following. Try to use only the information provided. Try to include as many key details as possible.\n
{context_str}\n
SUMMARY:\n
    """,

    "llm_summarize_prompt": """
You are an efficient Document Compressor. Your task is to read the document provided below and extract its key information.

### Instructions
1.  Identify and list the main facts, figures, names, and core concepts from the text.
2.  Present these points as a concise, factual list.
3.  Do not add any information, opinions, or interpretations not present in the original text.
4.  The output should be a dense, information-rich summary.

### Document to Compress
{document}

### Compressed Summary
    """
}

GENERATOR_PROMPTS = {
    "system_prompt": """
    You are a helpful assistant that answers questions based on the provided context.
    """
}