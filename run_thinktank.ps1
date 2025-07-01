# UltimateThinktank - AI Think Tank Launcher
# PowerShell Script for Windows

param(
    [string]$Topic = "",
    [switch]$Interactive = $true,
    [switch]$SetupNotion = $false,
    [switch]$NoNotion = $false
)

# Set console title and colors
$Host.UI.RawUI.WindowTitle = "UltimateThinktank - AI Think Tank"
$Host.UI.RawUI.ForegroundColor = "Green"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    UltimateThinktank - AI Think Tank" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.10+ and try again" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if we're in the right directory
if (-not (Test-Path "src\ultimate_thinktank\main.py")) {
    Write-Host "❌ ERROR: Please run this script from the ultimate_thinktank project directory" -ForegroundColor Red
    Write-Host ""
    Write-Host "Current directory: $(Get-Location)" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Make sure you're in the folder containing the 'src' directory" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "⚠️  WARNING: No .env file found" -ForegroundColor Yellow
    Write-Host "You may need to set up your OpenAI API key and Notion integration" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Create a .env file with:" -ForegroundColor Cyan
    Write-Host "OPENAI_API_KEY=your_openai_key_here" -ForegroundColor White
    Write-Host "NOTION_TOKEN=your_notion_token_here" -ForegroundColor White
    Write-Host "NOTION_DATABASE_ID=your_database_id_here" -ForegroundColor White
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/N)"
    if ($continue -ne "y" -and $continue -ne "Y") {
        exit 0
    }
}

# Activate virtual environment if it exists
if (Test-Path ".venv\Scripts\Activate.ps1") {
    Write-Host "✓ Activating virtual environment..." -ForegroundColor Green
    & .\.venv\Scripts\Activate.ps1
} else {
    Write-Host "ℹ️  No virtual environment found, using system Python..." -ForegroundColor Yellow
}

# Build command arguments
$args = @()

if ($SetupNotion) {
    $args += "--setup-notion"
} elseif ($NoNotion) {
    $args += "--no-notion"
} elseif ($Topic -ne "") {
    $args += "--topic"
    $args += $Topic
} else {
    $args += "--interactive"
}

# Run the think tank
Write-Host ""
Write-Host "🚀 Starting think tank session..." -ForegroundColor Green
Write-Host ""

try {
    python -m src.ultimate_thinktank.main @args
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ Think tank session completed successfully!" -ForegroundColor Green
        Write-Host "Check your project folder for the report file." -ForegroundColor Cyan
    } else {
        Write-Host ""
        Write-Host "❌ Think tank encountered an error (Exit code: $LASTEXITCODE)" -ForegroundColor Red
    }
} catch {
    Write-Host ""
    Write-Host "❌ ERROR: Failed to run think tank" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Common solutions:" -ForegroundColor Yellow
    Write-Host "1. Make sure your .env file has the correct API keys" -ForegroundColor White
    Write-Host "2. Check your internet connection" -ForegroundColor White
    Write-Host "3. Ensure all dependencies are installed" -ForegroundColor White
}

Write-Host ""
Read-Host "Press Enter to exit" 