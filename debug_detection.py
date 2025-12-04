"""
Debug script to diagnose hand detection issues
"""

import cv2
import mediapipe as mp
import time

print("🔍 Hand Detection Diagnostic Tool")
print("="*60)

# Test 1: Camera
print("\n1️⃣ Testing Camera...")
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("   ❌ Camera at index 1 not available")
    print("   💡 Try running: find_camera.py")
    exit(1)

ret, frame = cap.read()
if not ret:
    print("   ❌ Cannot read from camera")
    exit(1)

print(f"   ✅ Camera working: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")

# Test 2: MediaPipe initialization
print("\n2️⃣ Testing MediaPipe...")
try:
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,  # Lower threshold
        min_tracking_confidence=0.5
    )
    print("   ✅ MediaPipe initialized")
except Exception as e:
    print(f"   ❌ MediaPipe error: {e}")
    exit(1)

# Test 3: Hand detection
print("\n3️⃣ Testing Hand Detection (20 seconds)...")
print("   👋 Show your hand to the camera NOW!")
print("   💡 Tips:")
print("      - Palm facing camera")
print("      - Hand clearly visible")
print("      - Good lighting")
print("      - 30-60cm from camera")
print()

start_time = time.time()
frames_processed = 0
hands_detected = 0
detection_times = []

try:
    while time.time() - start_time < 20:
        ret, frame = cap.read()
        if not ret:
            print("   ❌ Lost camera connection")
            break
        
        frames_processed += 1
        
        # Flip horizontally
        frame = cv2.flip(frame, 1)
        
        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process
        detection_start = time.time()
        results = hands.process(rgb_frame)
        detection_time = (time.time() - detection_start) * 1000
        detection_times.append(detection_time)
        
        # Check results
        if results.multi_hand_landmarks:
            hands_detected += 1
            for hand_landmarks in results.multi_hand_landmarks:
                # Get some landmark positions
                wrist = hand_landmarks.landmark[0]
                index_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]
                
                print(f"   ✋ HAND DETECTED (frame {frames_processed}):")
                print(f"      Wrist: ({wrist.x:.2f}, {wrist.y:.2f})")
                print(f"      Index: ({index_tip.x:.2f}, {index_tip.y:.2f})")
                print(f"      Thumb: ({thumb_tip.x:.2f}, {thumb_tip.y:.2f})")
                print(f"      Detection time: {detection_time:.1f}ms")
                print()
        
        # Progress indicator
        if frames_processed % 30 == 0:
            elapsed = time.time() - start_time
            print(f"   ⏱️  {elapsed:.0f}s elapsed... {hands_detected}/{frames_processed} frames with hands")
        
        time.sleep(0.05)  # ~20 FPS

except KeyboardInterrupt:
    print("\n   ⚠️  Interrupted by user")

finally:
    cap.release()
    hands.close()

# Results
print("\n" + "="*60)
print("📊 DIAGNOSTIC RESULTS:")
print("="*60)
print(f"Frames processed:     {frames_processed}")
print(f"Hands detected:       {hands_detected}")
print(f"Detection rate:       {(hands_detected/frames_processed*100):.1f}%")
print(f"Avg detection time:   {sum(detection_times)/len(detection_times):.1f}ms")
print()

# Diagnosis
if hands_detected == 0:
    print("❌ NO HANDS DETECTED")
    print("\n💡 Possible Issues:")
    print("   1. Hand not visible to camera")
    print("   2. Poor lighting conditions")
    print("   3. Hand too far or too close (try 30-60cm)")
    print("   4. Camera pointed wrong direction")
    print("   5. Hand not showing palm/fingers clearly")
    print("\n🔧 Try These:")
    print("   • Open DroidCam app on phone - check camera view")
    print("   • Make sure you can see your hand in DroidCam")
    print("   • Turn on lights / improve lighting")
    print("   • Hold hand with palm facing camera")
    print("   • Spread fingers apart")
    
elif hands_detected < frames_processed * 0.3:
    print("⚠️  LOW DETECTION RATE")
    print("\n💡 Detection is working but inconsistent")
    print("\n🔧 Try These:")
    print("   • Improve lighting")
    print("   • Keep hand more stable")
    print("   • Keep palm facing camera")
    print("   • Move closer to camera (but not too close)")
    
else:
    print("✅ HAND DETECTION WORKING!")
    print("\n🎉 Your setup is good!")
    print("\n🚀 Ready to run: hand_mouse_no_gui.py")
    print("\n⚙️  If tracking seems off, adjust these in config.py:")
    print("   MIN_DETECTION_CONFIDENCE = 0.5")
    print("   MIN_TRACKING_CONFIDENCE = 0.5")

print("\n" + "="*60)
