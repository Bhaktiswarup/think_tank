#!/usr/bin/env python
"""
Wrapper script to run the UltimateThinktank with proper command line argument handling.
This allows 'crewai run' to work with interactive mode and custom topics.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ultimate_thinktank.main import run

def main():
    """Main function that can be called by the scripts"""
    # Check if any arguments were passed
    if len(sys.argv) > 1:
        # If arguments are passed, run with those arguments
        run()
    else:
        # If no arguments, default to interactive mode
        print("🤖 UltimateThinktank - No topic specified, starting interactive mode...")
        # Set up sys.argv to simulate --interactive
        sys.argv = [sys.argv[0], '--interactive']
        run()

if __name__ == "__main__":
    main() 