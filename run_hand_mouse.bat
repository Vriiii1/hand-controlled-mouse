@echo off
cd /d "%~dp0"
echo ========================================
echo   Hand-Controlled Mouse
echo ========================================
echo.
echo Starting application...
echo Press Ctrl+C to stop
echo.
.\venv\Scripts\python.exe hand_mouse_no_gui.py
pause
