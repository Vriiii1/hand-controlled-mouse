@echo off
echo Restarting DroidCam Virtual Camera...
echo.
echo Step 1: Close DroidCam Client
taskkill /F /IM DroidCam.exe 2>nul
taskkill /F /IM DroidCamApp.exe 2>nul
timeout /t 2 >nul

echo Step 2: Restart DroidCam service
net stop "DroidCam Source 3" 2>nul
timeout /t 2 >nul
net start "DroidCam Source 3" 2>nul
timeout /t 2 >nul

echo.
echo Done! Now:
echo 1. Open DroidCam Client on PC
echo 2. Reconnect to your iPhone
echo 3. Run the test again
echo.
pause
