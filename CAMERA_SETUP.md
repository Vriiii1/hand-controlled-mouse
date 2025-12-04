# 📱 Camera Setup Guide

## Issue: No Camera Detected

You're seeing this error because no webcam is currently connected to your computer.

## Solution: Use iPhone as Webcam

You mentioned using your iPhone as a webcam. Here are the setup instructions:

---

## Option 1: EpocCam (Recommended)

### Download & Install

1. **On iPhone**:
   - Open App Store
   - Search for "EpocCam Webcam for Mac and PC"
   - Download and install (Free version available)

2. **On Windows PC**:
   - Go to: https://www.elgato.com/us/en/s/epoccam
   - Download "EpocCam Drivers for Windows"
   - Install the drivers
   - **Restart your computer** (important!)

### Connect

1. Connect iPhone and PC to the **same WiFi network**
2. Open EpocCam app on iPhone
3. The app should automatically connect
4. Your iPhone will now appear as a webcam!

### Verify in Python

```python
import cv2

# Try different camera indices
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"✅ Camera found at index {i}")
        cap.release()
    else:
        print(f"❌ No camera at index {i}")
```

---

## Option 2: DroidCam

### Download & Install

1. **On iPhone**:
   - Open App Store
   - Search for "DroidCam Webcam & OBS Camera"
   - Download and install

2. **On Windows PC**:
   - Go to: https://www.dev47apps.com/droidcam/windows/
   - Download "DroidCam Client"
   - Install the software

### Connect

1. Open DroidCam on iPhone - note the IP address shown
2. Open DroidCam Client on PC
3. Enter the IP address from your phone
4. Click "Start"
5. Your iPhone is now a webcam!

---

## Option 3: iVCam

### Download & Install

1. **On iPhone**:
   - Open App Store
   - Search for "iVCam Webcam"
   - Download and install

2. **On Windows PC**:
   - Go to: https://www.e2esoft.com/ivcam/
   - Download "iVCam Client Software"
   - Install the software

### Connect

1. Connect iPhone via USB cable OR same WiFi
2. Open iVCam on iPhone
3. Open iVCam on PC
4. They should connect automatically

---

## Option 4: Use Built-in Webcam (If Available)

If your laptop has a built-in webcam:
- No setup needed!
- Just make sure no other apps are using it
- The camera should work at index 0

---

## Find Your Camera Index

After setting up your iPhone as webcam, run this test:

```powershell
cd handDetection
python test_camera.py
```

If camera index 0 doesn't work, try these:

```python
# Edit config.py and change CAMERA_INDEX:
CAMERA_INDEX = 1  # Try 1, 2, 3, etc.
```

---

## Common Issues

### Issue: "Camera not found"
**Solution**: 
- Make sure the webcam app is running on iPhone
- Restart the PC after installing drivers
- Check that iPhone and PC are on same WiFi
- Try different camera indices (0, 1, 2, 3)

### Issue: "Permission denied"
**Solution**:
- Check Windows camera permissions: Settings → Privacy → Camera
- Make sure apps can access your camera

### Issue: "Low FPS or laggy"
**Solution**:
- Use USB connection instead of WiFi (if app supports it)
- Close other apps using the camera
- Reduce camera resolution in config.py

### Issue: EpocCam shows black screen
**Solution**:
- Make sure both devices on same network
- Restart both apps
- Reinstall drivers on PC

---

## Test Your Setup

Once camera is connected, run:

```powershell
# Test camera only
python test_camera.py

# Test full hand detection
python hand_mouse.py
```

---

## Recommended Settings for iPhone Camera

In `config.py`, adjust these settings for best performance:

```python
# For WiFi connection (may be slower)
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
SMOOTHING_FRAMES = 7  # More smoothing for network latency

# For USB connection (faster)
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720
SMOOTHING_FRAMES = 5  # Less smoothing needed
```

---

## Ready to Proceed?

1. ✅ Choose a webcam app (EpocCam recommended)
2. ✅ Install on both iPhone and PC
3. ✅ Connect them
4. ✅ Run `python test_camera.py` to verify
5. ✅ Run `python hand_mouse.py` to start!

---

**Need help?** Open an issue on GitHub with:
- Your webcam app name
- Error messages
- Camera index you tried
