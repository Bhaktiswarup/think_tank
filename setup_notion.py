#!/usr/bin/env python
"""
Notion Setup Script for UltimateThinktank

This script helps you set up Notion integration for storing think tank discussions.
"""

import os
import sys
from notion_client import Client
from src.ultimate_thinktank.tools.notion_tools import create_notion_database_schema

def setup_notion_integration():
    """Guide user through Notion setup process"""
    
    print("🚀 UltimateThinktank Notion Integration Setup")
    print("=" * 50)
    
    # Check if environment variables are already set
    notion_token = os.getenv("NOTION_TOKEN")
    database_id = os.getenv("NOTION_DATABASE_ID")
    
    if notion_token and database_id:
        print("✅ Notion integration already configured!")
        print(f"Token: {notion_token[:10]}...")
        print(f"Database ID: {database_id}")
        return True
    
    print("\n📋 To set up Notion integration, you'll need:")
    print("1. A Notion integration token")
    print("2. A Notion database ID")
    print("3. To add these to your .env file")
    
    # Get Notion token
    print("\n🔑 Step 1: Get your Notion Integration Token")
    print("1. Go to https://www.notion.so/my-integrations")
    print("2. Click 'New integration'")
    print("3. Give it a name (e.g., 'UltimateThinktank')")
    print("4. Select the workspace where you want to create the database")
    print("5. Copy the 'Internal Integration Token'")
    
    token = input("\nEnter your Notion integration token: ").strip()
    if not token:
        print("❌ Token is required. Please run the setup again.")
        return False
    
    # Test the token
    try:
        client = Client(auth=token)
        # Try to get user info to verify token
        user = client.users.me()
        print(f"✅ Token verified! Connected as: {user.get('name', 'Unknown')}")
    except Exception as e:
        print(f"❌ Invalid token: {e}")
        return False
    
    # Create database
    print("\n🗄️ Step 2: Create Notion Database")
    print("We'll create a database with the recommended schema for think tank discussions.")
    
    parent_page = input("Enter the page ID where you want to create the database (or press Enter to use your workspace root): ").strip()
    
    try:
        schema = create_notion_database_schema()
        
        if parent_page:
            parent = {"page_id": parent_page}
        else:
            # Use workspace root
            parent = {"type": "workspace"}
        
        database = client.databases.create(
            parent=parent,
            title=[{"type": "text", "text": {"content": "UltimateThinktank Discussions"}}],
            properties=schema
        )
        
        database_id = database["id"]
        print(f"✅ Database created successfully!")
        print(f"Database ID: {database_id}")
        print(f"Database URL: https://notion.so/{database_id.replace('-', '')}")
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return False
    
    # Save to .env file
    print("\n💾 Step 3: Save Configuration")
    
    env_content = f"""# Notion Integration
NOTION_TOKEN={token}
NOTION_DATABASE_ID={database_id}

# OpenAI API Key (if not already set)
# OPENAI_API_KEY=your_openai_api_key_here
"""
    
    # Check if .env file exists
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            existing_content = f.read()
        
        # Check if Notion variables already exist
        if "NOTION_TOKEN" in existing_content:
            print("⚠️ Notion variables already exist in .env file")
            overwrite = input("Do you want to overwrite them? (y/N): ").strip().lower()
            if overwrite != 'y':
                print("Setup cancelled.")
                return False
        
        # Append new content
        with open(".env", "a") as f:
            f.write("\n" + env_content)
    else:
        # Create new .env file
        with open(".env", "w") as f:
            f.write(env_content)
    
    print("✅ Configuration saved to .env file!")
    
    # Test the setup
    print("\n🧪 Step 4: Testing Integration")
    try:
        os.environ["NOTION_TOKEN"] = token
        os.environ["NOTION_DATABASE_ID"] = database_id
        
        from src.ultimate_thinktank.tools.notion_tools import GetDiscussionHistory
        tool = GetDiscussionHistory()
        result = tool._run(1)
        print("✅ Integration test successful!")
        print(f"Test result: {result}")
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False
    
    print("\n🎉 Notion integration setup complete!")
    print("\n📝 Next steps:")
    print("1. Make sure your .env file is in the project root")
    print("2. Run your think tank: crewai run --interactive")
    print("3. Discussions will automatically be stored in your Notion database")
    
    return True

def create_sample_database():
    """Create a sample database with example data"""
    
    print("\n📊 Creating sample database with example discussions...")
    
    try:
        from src.ultimate_thinktank.tools.notion_tools import StoreThinkTankDiscussion
        
        # Sample discussion data
        sample_data = {
            "visionary_thinker": "AI-powered personalized education could revolutionize learning by adapting to each student's unique needs and learning style.",
            "critical_analyst": "Key challenges include data privacy concerns, implementation costs, and ensuring equitable access across different socioeconomic groups.",
            "practical_implementer": "Phase 1: Pilot program in 3 schools. Phase 2: Expand to 50 schools. Phase 3: Full deployment with continuous improvement.",
            "market_expert": "Education technology market is growing at 15% annually. Key competitors include Duolingo, Coursera, and Khan Academy.",
            "technical_specialist": "Requires machine learning models for personalization, secure data storage, and scalable cloud infrastructure.",
            "synthesis_coordinator": "AI education platform shows strong potential with careful attention to privacy, accessibility, and gradual rollout."
        }
        
        final_report = """
# AI-Powered Education Platform Analysis

## Executive Summary
The proposed AI-powered education platform shows significant potential for transforming learning experiences while requiring careful attention to implementation challenges.

## Key Recommendations
1. Start with a pilot program in 3 diverse schools
2. Implement robust data privacy measures from day one
3. Ensure equitable access through strategic partnerships
4. Build scalable technical infrastructure
5. Establish continuous feedback loops for improvement

## Next Steps
- Develop detailed technical specifications
- Create privacy and security protocols
- Identify pilot school partners
- Secure initial funding for development
        """
        
        tool = StoreThinkTankDiscussion()
        result = tool._run("AI-Powered Education Platform", sample_data, final_report)
        print(f"✅ Sample discussion created: {result}")
        
    except Exception as e:
        print(f"❌ Error creating sample: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        create_sample_database()
    else:
        setup_notion_integration() 