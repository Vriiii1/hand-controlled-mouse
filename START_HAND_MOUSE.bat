@echo off
cd /d "%~dp0"
cls
echo.
echo ========================================
echo   HAND-CONTROLLED MOUSE
echo ========================================
echo.
echo Camera: iVCam (Index 1)
echo.
echo Controls:
echo   - Move index finger to control cursor
echo   - Pinch thumb + index for left click
echo   - Pinch thumb + middle for right click
echo   - Open palm and move up/down to scroll
echo   - Press Ctrl+C to stop
echo.
echo ========================================
echo.
echo Starting...
echo.

.\venv\Scripts\python.exe hand_mouse_no_gui.py

echo.
echo Application stopped.
pause
