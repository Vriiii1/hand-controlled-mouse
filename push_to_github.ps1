#!/usr/bin/env pwsh
# PowerShell script to initialize and push project to GitHub

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "🖐️  Hand-Controlled Mouse - GitHub Setup" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if git is installed
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git is not installed. Please install Git first." -ForegroundColor Red
    Write-Host "Download from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Git is installed" -ForegroundColor Green

# Check if already a git repository
if (Test-Path .git) {
    Write-Host "`n⚠️  Git repository already exists." -ForegroundColor Yellow
    $response = Read-Host "Do you want to reinitialize? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Host "Skipping git init..." -ForegroundColor Yellow
    } else {
        Remove-Item -Recurse -Force .git
        git init
        Write-Host "✅ Reinitialized git repository" -ForegroundColor Green
    }
} else {
    git init
    Write-Host "✅ Initialized git repository" -ForegroundColor Green
}

# Add all files
Write-Host "`n📦 Adding files to git..." -ForegroundColor Cyan
git add .

# Check if there are changes to commit
$status = git status --porcelain
if ($status) {
    Write-Host "✅ Files added successfully" -ForegroundColor Green
    
    # Commit
    Write-Host "`n💾 Creating initial commit..." -ForegroundColor Cyan
    git commit -m "Initial commit: Hand-controlled mouse project setup"
    Write-Host "✅ Initial commit created" -ForegroundColor Green
} else {
    Write-Host "⚠️  No changes to commit" -ForegroundColor Yellow
}

# Ask for GitHub username (default: Vriiii1)
Write-Host "`n👤 GitHub Setup" -ForegroundColor Cyan
$username = Read-Host "Enter your GitHub username (default: Vriiii1)"
if ([string]::IsNullOrWhiteSpace($username)) {
    $username = "Vriiii1"
}

# Ask for repository name
$repoName = Read-Host "Enter repository name (default: hand-controlled-mouse)"
if ([string]::IsNullOrWhiteSpace($repoName)) {
    $repoName = "hand-controlled-mouse"
}

# Construct remote URL
$remoteUrl = "https://github.com/$username/$repoName.git"

# Check if remote already exists
$existingRemote = git remote get-url origin 2>$null
if ($existingRemote) {
    Write-Host "`n⚠️  Remote 'origin' already exists: $existingRemote" -ForegroundColor Yellow
    $response = Read-Host "Do you want to update it? (y/N)"
    if ($response -eq "y" -or $response -eq "Y") {
        git remote remove origin
        git remote add origin $remoteUrl
        Write-Host "✅ Updated remote origin" -ForegroundColor Green
    }
} else {
    git remote add origin $remoteUrl
    Write-Host "✅ Added remote origin: $remoteUrl" -ForegroundColor Green
}

# Set main branch
git branch -M main
Write-Host "✅ Set branch to 'main'" -ForegroundColor Green

# Push to GitHub
Write-Host "`n🚀 Pushing to GitHub..." -ForegroundColor Cyan
Write-Host "Repository: $remoteUrl" -ForegroundColor Yellow
Write-Host "`n⚠️  You may be prompted for credentials:" -ForegroundColor Yellow
Write-Host "   Username: $username" -ForegroundColor White
Write-Host "   Password: Use your Personal Access Token (not your GitHub password)" -ForegroundColor White
Write-Host "`nTo create a token: GitHub → Settings → Developer settings → Personal access tokens`n" -ForegroundColor Gray

$response = Read-Host "Ready to push? (Y/n)"
if ($response -eq "n" -or $response -eq "N") {
    Write-Host "`n⏸️  Push cancelled. You can push manually later with:" -ForegroundColor Yellow
    Write-Host "   git push -u origin main" -ForegroundColor White
    exit 0
}

try {
    git push -u origin main
    Write-Host "`n✅ Successfully pushed to GitHub!" -ForegroundColor Green
    Write-Host "`n🎉 Your repository is now live at:" -ForegroundColor Cyan
    Write-Host "   https://github.com/$username/$repoName" -ForegroundColor White
    
    Write-Host "`n📋 Next Steps:" -ForegroundColor Cyan
    Write-Host "   1. Visit your repository and add a description" -ForegroundColor White
    Write-Host "   2. Add topics: hand-tracking, gesture-control, mediapipe, opencv, python" -ForegroundColor White
    Write-Host "   3. Install dependencies: pip install -r requirements.txt" -ForegroundColor White
    Write-Host "   4. Run the app: python hand_mouse.py" -ForegroundColor White
    
} catch {
    Write-Host "`n❌ Failed to push to GitHub" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host "`n💡 Troubleshooting:" -ForegroundColor Yellow
    Write-Host "   1. Make sure the repository exists on GitHub" -ForegroundColor White
    Write-Host "   2. Verify your credentials (use Personal Access Token)" -ForegroundColor White
    Write-Host "   3. Check internet connection" -ForegroundColor White
    Write-Host "`nCreate the repository at: https://github.com/new" -ForegroundColor Gray
    Write-Host "Then run: git push -u origin main" -ForegroundColor White
}

Write-Host "`n========================================`n" -ForegroundColor Cyan
