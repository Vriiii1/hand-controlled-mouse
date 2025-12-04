# 🚀 Setup Instructions for GitHub

## Step 1: Initialize Git Repository

Open PowerShell in the `handDetection` folder and run:

```powershell
cd handDetection
git init
git add .
git commit -m "Initial commit: Hand-controlled mouse project setup"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com/Vriiii1
2. Click the **"+"** icon in the top right → **"New repository"**
3. Repository name: `hand-controlled-mouse`
4. Description: `🖐️ Control your mouse with hand gestures using webcam and MediaPipe`
5. Choose **Public** or **Private**
6. **DO NOT** initialize with README, .gitignore, or license (we already have them)
7. Click **"Create repository"**

## Step 3: Push to GitHub

After creating the repository, run these commands:

```powershell
git remote add origin https://github.com/Vriiii1/hand-controlled-mouse.git
git branch -M main
git push -u origin main
```

If prompted for credentials:
- Username: `Vriiii1`
- Password: Use a **Personal Access Token** (not your GitHub password)

### Creating a Personal Access Token (if needed):
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → Select `repo` scope → Generate
3. Copy the token and use it as your password

## Step 4: Verify Upload

Visit your repository: https://github.com/Vriiii1/hand-controlled-mouse

You should see all files uploaded!

## Quick Commands Reference

```powershell
# Check git status
git status

# View commit history
git log --oneline

# Check remote URL
git remote -v

# Pull latest changes
git pull origin main

# Push new changes
git add .
git commit -m "Your commit message"
git push origin main
```

## 🎉 Next Steps After Setup

1. **Test the application locally**:
   ```powershell
   cd handDetection
   pip install -r requirements.txt
   python hand_mouse.py
   ```

2. **Add a repository description** on GitHub
3. **Add topics/tags**: `hand-tracking`, `gesture-control`, `mediapipe`, `opencv`, `python`, `computer-vision`
4. **Enable GitHub Actions** (already configured in `.github/workflows/`)
5. **Start developing** based on the plan!

## Troubleshooting

### Issue: "Permission denied"
**Solution**: Use HTTPS with Personal Access Token or set up SSH keys

### Issue: "Remote origin already exists"
**Solution**: 
```powershell
git remote remove origin
git remote add origin https://github.com/Vriiii1/hand-controlled-mouse.git
```

### Issue: Can't push to GitHub
**Solution**: Make sure you have push access to the repository and your token has `repo` permissions
