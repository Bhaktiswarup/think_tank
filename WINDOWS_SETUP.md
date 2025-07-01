# UltimateThinktank - Windows Setup Guide

This guide shows you how to set up and run your UltimateThinktank on Windows with simple double-click scripts.

## 🚀 Quick Start

### Option 1: Simple Batch File (Recommended)
1. **Double-click** `run_thinktank.bat` in your project folder
2. The script will automatically start the interactive think tank
3. Enter your topic when prompted

### Option 2: PowerShell Script (Advanced)
1. **Right-click** `run_thinktank.ps1` and select "Run with PowerShell"
2. Or open PowerShell and run: `.\run_thinktank.ps1`

### Option 3: Create Desktop Shortcut
1. **Double-click** `create_desktop_shortcut.bat`
2. This creates a shortcut on your desktop
3. **Double-click** the desktop shortcut anytime to run the think tank

## 📁 Available Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `run_thinktank.bat` | Simple batch file for basic usage | Double-click to run |
| `run_thinktank.ps1` | PowerShell script with advanced features | Right-click → Run with PowerShell |
| `create_desktop_shortcut.bat` | Creates desktop shortcut | Run once to create shortcut |

## ⚙️ PowerShell Script Options

The PowerShell script supports command-line arguments:

```powershell
# Interactive mode (default)
.\run_thinktank.ps1

# Specific topic
.\run_thinktank.ps1 -Topic "AI for climate change"

# Setup Notion integration
.\run_thinktank.ps1 -SetupNotion

# Run without Notion
.\run_thinktank.ps1 -NoNotion
```

## 🔧 Prerequisites

Before running the scripts, make sure you have:

1. **Python 3.10+** installed and in your PATH
2. **`.env` file** with your API keys:
   ```
   OPENAI_API_KEY=your_openai_key_here
   NOTION_TOKEN=your_notion_token_here
   NOTION_DATABASE_ID=your_database_id_here
   ```
3. **Dependencies installed** (run `pip install -r requirements.txt` or `pip install crewai[tools] notion-client duckduckgo-search`)

## 🎯 What Happens When You Run

1. **Script checks** for Python installation
2. **Validates** you're in the correct directory
3. **Checks** for `.env` file and warns if missing
4. **Activates** virtual environment if it exists
5. **Starts** the interactive think tank
6. **Shows** success/error messages

## 🛠️ Troubleshooting

### "Python is not installed"
- Install Python 3.10+ from [python.org](https://python.org)
- Make sure to check "Add Python to PATH" during installation

### "Please run this script from the ultimate_thinktank project directory"
- Make sure you're in the folder containing the `src` directory
- The script must be run from the project root

### "No .env file found"
- Create a `.env` file in the project root
- Add your API keys as shown above

### "Think tank encountered an error"
- Check your internet connection
- Verify your API keys are correct
- Ensure all dependencies are installed

## 🎨 Customization

### Change Default Behavior
Edit `run_thinktank.bat` or `run_thinktank.ps1` to:
- Change the default topic
- Add custom error messages
- Modify the startup checks

### Create Custom Shortcuts
You can create shortcuts for specific topics:
```batch
# Create a shortcut for a specific topic
python -m src.ultimate_thinktank.main --topic "Your favorite topic"
```

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Try running the Python command directly: `python -m src.ultimate_thinktank.main --interactive`

## 🎉 Enjoy Your Think Tank!

Once set up, you can:
- **Double-click** to start anytime
- **Enter any topic** for discussion
- **Get comprehensive analysis** from 6 AI agents
- **Store results** in Notion database
- **Build knowledge** over time

Your UltimateThinktank is now just a double-click away! 🚀 