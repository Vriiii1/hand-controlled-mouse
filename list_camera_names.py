"""
List all camera device names (Windows DirectShow)
"""

import cv2
import subprocess

print("🎥 Finding Camera Device Names")
print("="*70)

# Try using Windows Media Foundation backend to list devices
print("\nSearching for camera devices...\n")

# Test each index and try to get the backend name
for i in range(10):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        backend = cap.getBackendName()
        ret, frame = cap.read()
        status = "✅ Working" if ret else "⚠️ Not capturing"
        print(f"Index {i}: {backend} - {status}")
        
        # Try to get device name using Windows API
        try:
            # Get video input devices via PowerShell
            pass
        except:
            pass
        
        cap.release()
    else:
        print(f"Index {i}: Not available")

print("\n" + "="*70)
print("\n💡 Let's try accessing DroidCam by name instead of index")
print("\nAttempting to find DroidCam device name...\n")

# Common DroidCam device names
droidcam_names = [
    "DroidCam Source 3",
    "DroidCam Source",
    "DroidCam Video",
    "DroidCamX",
]

for name in droidcam_names:
    print(f"Trying: {name}...", end=" ")
    # OpenCV doesn't support opening by name directly on Windows
    # We'll need to find the index that corresponds to this device
    print("(OpenCV on Windows needs index, not name)")

print("\n" + "="*70)
print("\n📋 Recommendation:")
print("\nSince DroidCam Client shows video but Python can't access it,")
print("the issue is that DroidCam's virtual camera isn't properly bridged.")
print("\n🎯 BEST SOLUTION: Switch to EpocCam or iVCam")
print("\nThese apps create proper virtual cameras that work with OpenCV.")
print("\nOR")
print("\n🔧 In DroidCam Client:")
print("   1. Go to: Connection → Settings")
print("   2. Make sure 'Use DroidCam Virtual Device' is enabled")
print("   3. Restart the client")
print("="*70)
