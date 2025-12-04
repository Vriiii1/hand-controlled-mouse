#!/usr/bin/env pwsh
# Quick start script for Hand-Controlled Mouse

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "🖐️  Hand-Controlled Mouse - Quick Start" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check Python installation
Write-Host "🔍 Checking Python installation..." -ForegroundColor Cyan
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.9+ from: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

$pythonVersion = python --version
Write-Host "✅ Found: $pythonVersion" -ForegroundColor Green

# Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "✅ Virtual environment exists" -ForegroundColor Green
} else {
    Write-Host "`n📦 Creating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
    Write-Host "✅ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "`n🔌 Activating virtual environment..." -ForegroundColor Cyan
if ($IsWindows -or $env:OS -match "Windows") {
    & ".\venv\Scripts\Activate.ps1"
} else {
    & "./venv/bin/Activate.ps1"
}

# Install dependencies
Write-Host "`n📥 Installing dependencies..." -ForegroundColor Cyan
Write-Host "(This may take a few minutes...)" -ForegroundColor Gray

python -m pip install --upgrade pip
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Check camera
Write-Host "`n📷 Camera Check" -ForegroundColor Cyan
Write-Host "Make sure your webcam is connected and not in use by other applications." -ForegroundColor Yellow

# Run the application
Write-Host "`n🚀 Starting Hand-Controlled Mouse..." -ForegroundColor Cyan
Write-Host "`nControls:" -ForegroundColor Yellow
Write-Host "  • Move hand to control cursor" -ForegroundColor White
Write-Host "  • Pinch (thumb + index) for left click" -ForegroundColor White
Write-Host "  • Pinch (thumb + middle) for right click" -ForegroundColor White
Write-Host "  • Move hand up/down with open palm to scroll" -ForegroundColor White
Write-Host "  • Press 'q' to quit`n" -ForegroundColor White

$response = Read-Host "Ready to start? (Y/n)"
if ($response -eq "n" -or $response -eq "N") {
    Write-Host "`n⏸️  Start cancelled. Run manually with: python hand_mouse.py" -ForegroundColor Yellow
    exit 0
}

Write-Host "`n" + "="*50 -ForegroundColor Cyan
python hand_mouse.py

Write-Host "`n========================================`n" -ForegroundColor Cyan
