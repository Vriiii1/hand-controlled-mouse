# 🚀 Quick Start Guide

## ✅ Setup Complete!

Your hand-controlled mouse application is ready to use!

## 📱 Current Setup

- ✅ **Camera**: DroidCam at index 1
- ✅ **Python**: 3.10.11 (in virtual environment)
- ✅ **Dependencies**: All installed
- ✅ **GitHub**: https://github.com/Vriiii1/hand-controlled-mouse

## 🎮 How to Run

### Method 1: Double-click the batch file (Easiest)
```
Double-click: run_hand_mouse.bat
```

### Method 2: Command line
```powershell
cd E:\myPrompter\handDetection
.\venv\Scripts\python.exe hand_mouse_no_gui.py
```

### Method 3: With GUI (if display works)
```powershell
cd E:\myPrompter\handDetection
.\venv\Scripts\python.exe hand_mouse.py
```

## 🖐️ Using the Application

### Before You Start:
1. ✅ Make sure DroidCam is running on your iPhone
2. ✅ Make sure DroidCam client is connected on PC
3. ✅ Position your hand in front of the camera
4. ✅ Good lighting helps a lot!

### Controls:

**Cursor Movement:**
- Hold your hand up, palm facing camera
- Extend your **index finger**
- Move your hand to move the cursor

**Left Click:**
- Pinch **thumb** and **index finger** together
- Release to unclick

**Right Click:**
- Pinch **thumb** and **middle finger** together

**Scroll:**
- Open palm (all fingers extended)
- Move hand **up** to scroll up
- Move hand **down** to scroll down

**Stop the Application:**
- Press **Ctrl+C** in the terminal

## ⚙️ Adjusting Settings

Edit `config.py` to customize:

```python
# Make cursor move faster/slower
MOUSE_SPEED_MULTIPLIER = 1.5  # Increase for faster, decrease for slower

# Make gestures more/less sensitive
PINCH_THRESHOLD = 0.05  # Lower = need to pinch tighter

# Make cursor smoother
SMOOTHING_FRAMES = 5  # Higher = smoother but slower response

# Reduce jitter
DEAD_ZONE = 5  # Higher = less jittery but less precise
```

## 🐛 Troubleshooting

### Cursor is too fast/slow
Edit `config.py`:
```python
MOUSE_SPEED_MULTIPLIER = 1.0  # Try values between 0.5 and 2.0
```

### Gestures not detecting
Edit `config.py`:
```python
PINCH_THRESHOLD = 0.08  # Make it easier to detect
MIN_DETECTION_CONFIDENCE = 0.5  # Lower threshold
```

### Cursor is jittery
Edit `config.py`:
```python
SMOOTHING_FRAMES = 10  # More smoothing
DEAD_ZONE = 10  # Bigger dead zone
```

### Camera not found
1. Make sure DroidCam is running on both devices
2. Check they're on the same WiFi
3. Try running: `.\venv\Scripts\python.exe find_camera.py`
4. Update `CAMERA_INDEX` in config.py if needed

### Application crashes
1. Make sure no other app is using the camera
2. Close DroidCam and reopen it
3. Restart the Python script

## 📊 Test Scripts

### Test camera only:
```powershell
.\venv\Scripts\python.exe test_camera.py
```

### Test hand tracking:
```powershell
.\venv\Scripts\python.exe test_hand_tracking.py
```

### Find available cameras:
```powershell
.\venv\Scripts\python.exe find_camera.py
```

## 🎯 Tips for Best Performance

1. **Lighting**: Use good lighting, avoid backlighting
2. **Distance**: Keep hand 30-60cm from camera
3. **Background**: Plain background works better
4. **Hand position**: Palm facing camera, fingers clearly visible
5. **WiFi**: Use 5GHz WiFi for better DroidCam performance
6. **USB**: If possible, use USB connection in DroidCam for lower latency

## 📝 What Next?

Once you're comfortable with the basic controls:

1. **Calibrate**: Adjust thresholds in `config.py` for your hand
2. **Practice**: It takes a few minutes to get used to the gestures
3. **Customize**: Add your own gestures in `gestures.py`
4. **Share**: Show it off and get feedback!
5. **Contribute**: Submit improvements to GitHub

## 🔗 Quick Links

- **Repository**: https://github.com/Vriiii1/hand-controlled-mouse
- **Camera Setup**: CAMERA_SETUP.md
- **Full Documentation**: README.md
- **Project Status**: CURRENT_STATUS.md

## ❓ Need Help?

1. Check CAMERA_SETUP.md for camera issues
2. Check CURRENT_STATUS.md for setup status
3. Open an issue on GitHub
4. Review the code in hand_mouse_no_gui.py

---

## 🎉 Ready to Go!

**Run the application:**
```
Double-click: run_hand_mouse.bat
```

**Or:**
```powershell
.\venv\Scripts\python.exe hand_mouse_no_gui.py
```

**Have fun controlling your mouse with your hand!** 🖐️✨
