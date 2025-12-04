"""
Ultra simple hand detection test - just counts detections
"""

import cv2
import mediapipe as mp
import time

print("\n" + "="*60)
print("SIMPLE HAND DETECTION TEST")
print("="*60)
print("\nInstructions:")
print("  1. Make sure DroidCam is running and connected")
print("  2. Hold your hand in front of the camera")
print("  3. Palm facing camera, fingers visible")
print("  4. Test will run for 15 seconds")
print("\nStarting in 3 seconds...\n")
time.sleep(3)

# Initialize
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.3,  # Very low threshold
    min_tracking_confidence=0.3
)

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ ERROR: Cannot open camera at index 1")
    print("\n💡 Make sure:")
    print("   - DroidCam is running on phone")
    print("   - DroidCam client is running on PC")
    print("   - Both are connected")
    exit(1)

print("✅ Camera opened successfully\n")
print("Testing... (15 seconds)\n")

start = time.time()
frame_count = 0
detect_count = 0

while time.time() - start < 15:
    ret, frame = cap.read()
    if not ret:
        continue
    
    frame_count += 1
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    
    if results.multi_hand_landmarks:
        detect_count += 1
        print(f"✋ Hand detected! (Frame {frame_count}, Total: {detect_count})")
    
    if frame_count % 50 == 0:
        print(f"   ... {frame_count} frames processed, {detect_count} detections so far")
    
    time.sleep(0.033)  # ~30 FPS

cap.release()
hands.close()

print("\n" + "="*60)
print("RESULTS:")
print("="*60)
print(f"Total frames:      {frame_count}")
print(f"Hands detected:    {detect_count}")
print(f"Detection rate:    {(detect_count/frame_count*100):.1f}%")

if detect_count == 0:
    print("\n❌ NO HANDS DETECTED!")
    print("\n💡 Troubleshooting checklist:")
    print("   ☐ DroidCam app running on iPhone?")
    print("   ☐ DroidCam client connected on PC?")
    print("   ☐ Can you see yourself in DroidCam preview?")
    print("   ☐ Hand visible in camera view?")
    print("   ☐ Palm facing camera?")
    print("   ☐ Fingers clearly visible?")
    print("   ☐ Good lighting in room?")
    print("   ☐ Not too far from camera (try 40cm distance)?")
    print("\n🔧 Next steps:")
    print("   1. Open DroidCam on phone - check the camera preview")
    print("   2. Make sure you can see your hand clearly")
    print("   3. Try holding hand directly in front of camera")
    print("   4. Run this test again")
elif detect_count < frame_count * 0.3:
    print("\n⚠️  LOW DETECTION RATE")
    print("\n💡 Tips:")
    print("   • Improve lighting")
    print("   • Keep hand steady")
    print("   • Palm towards camera")
    print("   • Don't move too fast")
else:
    print("\n✅ DETECTION WORKING!")
    print("\nYou're ready to use the hand mouse!")
    print("Run: .\\venv\\Scripts\\python.exe hand_mouse_no_gui.py")

print("="*60 + "\n")
