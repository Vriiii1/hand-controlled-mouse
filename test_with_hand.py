"""
Test hand detection with visual feedback - saves images showing if hand detected
"""

import cv2
import mediapipe as mp
import time

print("🖐️ Hand Detection Test with Visual Feedback")
print("="*70)
print("\n📋 Instructions:")
print("   1. Hold your hand UP with palm facing the camera")
print("   2. Spread your fingers apart")
print("   3. Keep hand in center of camera view")
print("   4. About 40-50cm from camera")
print("\nStarting in 3 seconds... GET READY!")
print("="*70)
time.sleep(3)

# Initialize
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.3,
    min_tracking_confidence=0.3
)

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit(1)

print("\n🎥 Testing for 10 seconds...\n")

start = time.time()
frame_count = 0
detect_count = 0
last_detected = False

while time.time() - start < 10:
    ret, frame = cap.read()
    if not ret:
        continue
    
    frame_count += 1
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    
    if results.multi_hand_landmarks:
        detect_count += 1
        
        # Draw landmarks
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        if not last_detected:  # First detection
            print(f"✅ HAND DETECTED at frame {frame_count}!")
            cv2.imwrite(f"hand_detected_{detect_count}.jpg", frame)
            last_detected = True
    else:
        if last_detected:  # Lost detection
            print(f"   ... lost at frame {frame_count}")
            last_detected = False
    
    # Save periodic frames for debugging
    if frame_count in [10, 50, 100]:
        cv2.imwrite(f"debug_frame_{frame_count}.jpg", frame)
    
    time.sleep(0.05)  # 20 FPS

cap.release()
hands.close()

print("\n" + "="*70)
print("📊 RESULTS:")
print("="*70)
print(f"Total frames:      {frame_count}")
print(f"Hands detected:    {detect_count}")
print(f"Detection rate:    {(detect_count/frame_count*100):.1f}%")

if detect_count > 0:
    print(f"\n✅ SUCCESS! Hand detected {detect_count} times!")
    print(f"\n📁 Saved images:")
    print(f"   • hand_detected_*.jpg (images with hands)")
    print(f"   • debug_frame_*.jpg (sample frames)")
    print("\n🚀 Ready to run the full application!")
else:
    print("\n❌ NO HANDS DETECTED")
    print(f"\n📁 Check debug images:")
    print(f"   • debug_frame_10.jpg")
    print(f"   • debug_frame_50.jpg")  
    print(f"   • debug_frame_100.jpg")
    print("\n💡 Possible issues:")
    print("   • Hand not visible to camera")
    print("   • Too far from camera (try 40cm)")
    print("   • Poor lighting")
    print("   • Fingers not spread apart")
    print("   • Palm not facing camera")

print("="*70)
