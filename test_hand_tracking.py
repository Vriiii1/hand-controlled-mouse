"""
Simple test to verify hand tracking is working
"""

import cv2
import mediapipe as mp
import time

print("🖐️ Testing Hand Tracking...")
print("Show your hand to the camera for 10 seconds")
print("="*50 + "\n")

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
    max_num_hands=1
)

# Open camera
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("❌ Could not open camera")
    exit(1)

print("✅ Camera opened successfully")

start_time = time.time()
frame_count = 0
hand_detected_count = 0

try:
    while time.time() - start_time < 10:  # Run for 10 seconds
        success, frame = cap.read()
        if not success:
            print("❌ Failed to read frame")
            break
        
        frame_count += 1
        
        # Flip and convert
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process with MediaPipe
        results = hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            hand_detected_count += 1
            for hand_landmarks in results.multi_hand_landmarks:
                # Get index finger tip position
                index_tip = hand_landmarks.landmark[8]
                print(f"✋ Hand detected! Index finger at: ({index_tip.x:.3f}, {index_tip.y:.3f})")
        
        time.sleep(0.1)  # 10 FPS for testing

except KeyboardInterrupt:
    print("\n⚠️ Interrupted by user")

finally:
    cap.release()
    hands.close()

print("\n" + "="*50)
print(f"📊 Test Results:")
print(f"   Total frames: {frame_count}")
print(f"   Hands detected: {hand_detected_count}")
print(f"   Detection rate: {(hand_detected_count/frame_count*100):.1f}%")

if hand_detected_count > 0:
    print("\n✅ Hand tracking is working!")
    print("\n🚀 Ready to run: python hand_mouse_no_gui.py")
else:
    print("\n❌ No hands detected")
    print("\n💡 Tips:")
    print("   - Make sure your hand is visible to the camera")
    print("   - Check lighting conditions")
    print("   - Point your palm towards the camera")
