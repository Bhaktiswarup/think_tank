#!/usr/bin/env python
import sys
import warnings
import argparse
import os

from datetime import datetime

from ultimate_thinktank.crew import UltimateThinktank
from ultimate_thinktank.tools.notion_tools import StoreThinkTankDiscussion

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def check_notion_setup():
    """Check if Notion integration is properly configured"""
    notion_token = os.getenv("NOTION_TOKEN")
    database_id = os.getenv("NOTION_DATABASE_ID")
    
    if notion_token and database_id:
        return True, "✅ Notion integration configured"
    else:
        missing = []
        if not notion_token:
            missing.append("NOTION_TOKEN")
        if not database_id:
            missing.append("NOTION_DATABASE_ID")
        return False, f"⚠️ Missing Notion configuration: {', '.join(missing)}"

def run():
    """
    Run the think tank crew with user-specified topic.
    """
    parser = argparse.ArgumentParser(description='UltimateThinktank - Collaborative AI Think Tank')
    parser.add_argument('--topic', '-t', type=str, default='AI-powered education platforms',
                       help='Topic for the think tank to discuss (default: AI-powered education platforms)')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Run in interactive mode to input topic')
    parser.add_argument('--no-notion', action='store_true',
                       help='Disable Notion integration (discussions will only be saved locally)')
    parser.add_argument('--setup-notion', action='store_true',
                       help='Run Notion setup wizard')
    
    args = parser.parse_args()
    
    # Check for Notion setup
    if args.setup_notion:
        print("🔧 Running Notion setup wizard...")
        try:
            from setup_notion import setup_notion_integration
            setup_notion_integration()
            return
        except ImportError:
            print("❌ Setup script not found. Please run: python setup_notion.py")
            return
    
    notion_configured, notion_status = check_notion_setup()
    
    topic = args.topic
    
    if args.interactive:
        print("\n🤖 Welcome to the UltimateThinktank!")
        print("This is a collaborative AI think tank where 6 specialized agents will discuss your idea.")
        print("\nThe agents include:")
        print("• Visionary Thinker - Generates bold, innovative ideas")
        print("• Critical Analyst - Identifies risks and challenges")
        print("• Practical Implementer - Creates actionable plans")
        print("• Market Expert - Analyzes business viability")
        print("• Technical Specialist - Evaluates technical feasibility")
        print("• Synthesis Coordinator - Integrates all perspectives")
        
        print(f"\n{notion_status}")
        if not notion_configured and not args.no_notion:
            print("💡 Run with --setup-notion to configure Notion integration")
            print("💡 Or use --no-notion to run without Notion storage")
        
        topic = input("\n💡 What topic or idea would you like the think tank to explore? ")
        if not topic.strip():
            topic = "AI-powered education platforms"
            print(f"Using default topic: {topic}")
    
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    
    print(f"\n🚀 Starting think tank discussion on: {topic}")
    print("The agents will now engage in a collaborative discussion...\n")
    
    try:
        crew_instance = UltimateThinktank()
        result = crew_instance.crew().kickoff(inputs=inputs)
        print(f"\n✅ Think tank discussion completed!")
        print(f"📄 Full report saved as: thinktank_report.md")
        
        # Notion integration status
        if notion_configured and not args.no_notion:
            print(f"📊 Discussion automatically stored in Notion database")
            print(f"💡 Agents can now reference previous discussions in future sessions")

            # Store the full conversation transcript in Notion
            full_conversation = crew_instance.logger.get_transcript()
            # Use placeholders for discussion_data and final_report for now
            discussion_data = {}  # Optionally, extract actual agent outputs
            final_report = str(result)  # Or extract the summary if available
            notion_tool = StoreThinkTankDiscussion()
            notion_tool._run(topic, discussion_data, final_report, full_conversation)
        else:
            print(f"💾 Discussion saved locally only")
            if not args.no_notion:
                print(f"💡 Run --setup-notion to enable Notion storage")
        
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the think tank: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI-powered education platforms",
        'current_year': str(datetime.now().year)
    }
    try:
        UltimateThinktank().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        UltimateThinktank().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI-powered education platforms",
        "current_year": str(datetime.now().year)
    }
    
    try:
        UltimateThinktank().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
