#!/usr/bin/env python
"""
Example usage of the UltimateThinktank

This script demonstrates how to use the think tank with different topics.
"""

from ultimate_thinktank.crew import UltimateThinktank
from datetime import datetime

def run_think_tank_example(topic):
    """Run the think tank with a specific topic"""
    print(f"\n{'='*60}")
    print(f"🤖 THINK TANK DISCUSSION: {topic}")
    print(f"{'='*60}")
    
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = UltimateThinktank().crew().kickoff(inputs=inputs)
        print(f"\n✅ Discussion completed for: {topic}")
        print(f"📄 Report saved as: thinktank_report.md")
        return result
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    """Run example think tank discussions"""
    
    # Example topics for the think tank to explore
    example_topics = [
        "AI-powered personalized education platforms",
        "Sustainable urban transportation solutions",
        "Revolutionary social media platform",
        "Healthcare diagnostics using AI",
        "Renewable energy storage innovations"
    ]
    
    print("🚀 UltimateThinktank Examples")
    print("This will run the think tank on several example topics.")
    print("Each discussion will be saved to thinktank_report.md")
    
    for i, topic in enumerate(example_topics, 1):
        print(f"\n📋 Example {i}/{len(example_topics)}")
        run_think_tank_example(topic)
        
        # Add a small delay between runs
        import time
        time.sleep(2)
    
    print(f"\n🎉 All examples completed!")
    print("Check the generated thinktank_report.md files for results.")

if __name__ == "__main__":
    main() 