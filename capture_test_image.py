"""
Capture a test image from the camera to see what it's seeing
"""

import cv2
import time

print("📸 Camera Image Capture Test")
print("="*60)

# Open camera
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ Cannot open camera at index 1")
    print("\n💡 Check:")
    print("   • DroidCam running on phone?")
    print("   • DroidCam client running on PC?")
    print("   • Both connected?")
    exit(1)

print("✅ Camera opened successfully")
print(f"📺 Resolution: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")

# Let camera warm up
print("\n⏱️  Warming up camera (2 seconds)...")
time.sleep(2)

# Capture 5 frames
print("\n📸 Capturing test images...")
for i in range(5):
    ret, frame = cap.read()
    if ret:
        # Flip for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Save image
        filename = f"test_image_{i+1}.jpg"
        cv2.imwrite(filename, frame)
        print(f"   ✅ Saved: {filename}")
        time.sleep(0.5)
    else:
        print(f"   ❌ Failed to capture frame {i+1}")

cap.release()

print("\n" + "="*60)
print("✅ Test complete!")
print("\n📁 Check these files in your handDetection folder:")
print("   • test_image_1.jpg")
print("   • test_image_2.jpg")
print("   • test_image_3.jpg")
print("   • test_image_4.jpg")
print("   • test_image_5.jpg")
print("\n👀 Open the images and check:")
print("   • Is the image clear?")
print("   • Can you see your hand?")
print("   • Is lighting good?")
print("   • Are fingers clearly visible?")
print("\n💡 If images are:")
print("   • Blank/black: DroidCam not properly connected")
print("   • Blurry: Camera not focused / move slower")
print("   • Dark: Improve lighting")
print("   • No hand visible: Position hand in front of camera")
print("="*60 + "\n")
