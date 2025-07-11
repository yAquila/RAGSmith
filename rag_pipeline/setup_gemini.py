#!/usr/bin/env python3
"""
Setup script for Gemini integration.

This script helps users set up the Gemini API integration by:
1. Installing required dependencies
2. Guiding users through API key setup
3. Testing the integration
"""

import os
import sys
import subprocess
import getpass

def print_banner():
    """Print setup banner"""
    print("=" * 60)
    print("🚀 Gemini Integration Setup")
    print("=" * 60)
    print("This script will help you set up Google Gemini integration")
    print("for your RAG pipeline.")
    print()

def check_python_version():
    """Check if Python version is compatible"""
    print("📋 Checking Python version...")
    
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        print(f"Current version: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} is compatible")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    try:
        # Install google-generativeai
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "google-generativeai"
        ])
        print("✅ google-generativeai installed successfully")
        
        # Update requirements.txt if needed
        requirements_file = "requirements.txt"
        if os.path.exists(requirements_file):
            with open(requirements_file, 'r') as f:
                content = f.read()
            
            if "google-generativeai" not in content:
                print("📝 Updating requirements.txt...")
                with open(requirements_file, 'a') as f:
                    f.write("\n# Google Generative AI (for Gemini API)\n")
                    f.write("google-generativeai\n")
                print("✅ requirements.txt updated")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def get_api_key():
    """Get API key from user"""
    print("\n🔑 Setting up Gemini API key...")
    print("You need a Gemini API key from Google AI Studio:")
    print("1. Go to https://makersuite.google.com/app/apikey")
    print("2. Create a new API key")
    print("3. Copy the key")
    print()
    
    # Check if already set
    existing_key = os.getenv("GEMINI_API_KEY")
    if existing_key:
        print(f"✅ GEMINI_API_KEY already set: {existing_key[:10]}...")
        use_existing = input("Use existing key? (y/n): ").lower().strip()
        if use_existing == 'y':
            return existing_key
    
    # Get new key
    while True:
        api_key = getpass.getpass("Enter your Gemini API key: ").strip()
        
        if not api_key:
            print("❌ API key cannot be empty")
            continue
        
        if len(api_key) < 20:
            print("❌ API key seems too short")
            continue
        
        # Test the key
        print("🧪 Testing API key...")
        if test_api_key(api_key):
            return api_key
        else:
            print("❌ Invalid API key. Please try again.")

def test_api_key(api_key):
    """Test if the API key is valid"""
    try:
        import google.generativeai as genai
        
        # Configure with the key
        genai.configure(api_key=api_key)
        
        # Try to list models (this will fail if key is invalid)
        models = genai.list_models()
        
        # Check if we can find Gemini models
        gemini_models = [m for m in models if 'gemini' in m.name.lower()]
        
        if gemini_models:
            print(f"✅ API key is valid! Found {len(gemini_models)} Gemini models")
            return True
        else:
            print("❌ API key is valid but no Gemini models found")
            return False
            
    except Exception as e:
        print(f"❌ API key test failed: {e}")
        return False

def save_api_key(api_key):
    """Save API key to environment or file"""
    print("\n💾 Saving API key...")
    
    # Try to set environment variable
    try:
        os.environ["GEMINI_API_KEY"] = api_key
        print("✅ API key set in environment")
    except Exception as e:
        print(f"⚠️  Could not set environment variable: {e}")
    
    # Create .env file
    env_file = ".env"
    try:
        with open(env_file, 'w') as f:
            f.write(f"GEMINI_API_KEY={api_key}\n")
        print(f"✅ API key saved to {env_file}")
    except Exception as e:
        print(f"⚠️  Could not save to {env_file}: {e}")
    
    # Show instructions for manual setup
    print("\n📝 Manual setup instructions:")
    print("Add this line to your shell profile (~/.bashrc, ~/.zshrc, etc.):")
    print(f"export GEMINI_API_KEY='{api_key}'")

def run_test():
    """Run integration test"""
    print("\n🧪 Running integration test...")
    
    try:
        # Import and test
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        from util.api.gemini_client import GeminiUtil
        
        # Test simple response
        response = GeminiUtil.get_gemini_response(
            "gemini-1.5-flash",
            "What is 2+2? Please answer briefly."
        )
        
        if response and response.get('response'):
            print("✅ Integration test successful!")
            print(f"Response: {response['response']}")
            return True
        else:
            print("❌ Integration test failed")
            return False
            
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False

def show_next_steps():
    """Show next steps for the user"""
    print("\n🎉 Setup completed successfully!")
    print("\n📖 Next steps:")
    print("1. Test the integration:")
    print("   python test_gemini_integration.py")
    print()
    print("2. Run the example:")
    print("   python example_gemini_usage.py")
    print()
    print("3. Use in your RAG pipeline:")
    print("   from core.components import ComponentFactory")
    print("   gemini_gen = ComponentFactory.create_generation_component(")
    print("       'gemini-1.5-flash', config, 'gemini'")
    print("   )")
    print()
    print("4. Available models:")
    print("   - gemini-1.5-flash (fast, recommended)")
    print("   - gemini-1.5-pro (more capable)")
    print("   - gemini-2.0-flash-exp (experimental)")
    print("   - gemini-2.0-pro (most capable)")
    print()
    print("5. Free tier limits:")
    print("   - 100 requests/day with API key")
    print("   - 1,000 requests/day with Google account")

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Get API key
    api_key = get_api_key()
    if not api_key:
        print("❌ No valid API key provided")
        sys.exit(1)
    
    # Save API key
    save_api_key(api_key)
    
    # Run test
    if not run_test():
        print("❌ Integration test failed")
        sys.exit(1)
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    main() 