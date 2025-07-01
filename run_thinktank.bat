@echo off
cd /d %~dp0
title UltimateThinktank - AI Think Tank
color 0A

echo.
echo ========================================
echo    UltimateThinktank - AI Think Tank
echo ========================================
echo.
echo Starting your AI think tank...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ and try again
    pause
    exit /b 1
)

:: Check if we're in the right directory
if not exist "src\ultimate_thinktank\main.py" (
    echo ERROR: Please run this script from the ultimate_thinktank project directory
    echo.
    echo Current directory: %CD%
    echo.
    echo Make sure you're in the folder containing the 'src' directory
    pause
    exit /b 1
)

:: Check if .env file exists
if not exist ".env" (
    echo WARNING: No .env file found
    echo You may need to set up your OpenAI API key and Notion integration
    echo.
    echo Create a .env file with:
    echo OPENAI_API_KEY=your_openai_key_here
    echo NOTION_TOKEN=your_notion_token_here
    echo NOTION_DATABASE_ID=your_database_id_here
    echo.
    pause
)

:: Activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
) else (
    echo No virtual environment found, using system Python...
)

:: Run the think tank
echo.
echo Starting interactive think tank session...
echo.
python -m src.ultimate_thinktank.main --interactive

:: Check if the run was successful
if errorlevel 1 (
    echo.
    echo ERROR: Think tank encountered an error
    echo.
    echo Common solutions:
    echo 1. Make sure your .env file has the correct API keys
    echo 2. Check your internet connection
    echo 3. Ensure all dependencies are installed
    echo.
    pause
) else (
    echo.
    echo Think tank session completed successfully!
    echo Check your project folder for the report file.
    echo.
    pause
)
