"""
Quick camera test script to verify camera is working
"""

import cv2
import sys

print("🎥 Testing camera access...")
print("Press 'q' to quit\n")

# Try to open camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not open camera (index 0)")
    print("\n💡 Troubleshooting:")
    print("   1. Make sure no other application is using the camera")
    print("   2. Try a different camera index in config.py (1, 2, etc.)")
    print("   3. Check if camera permissions are enabled")
    print("   4. If using iPhone/EpocCam, make sure it's connected")
    sys.exit(1)

print("✅ Camera opened successfully!")
print(f"📊 Resolution: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
print("\nShowing camera feed... Press 'q' to quit\n")

frame_count = 0
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("❌ Failed to read frame from camera")
        break
    
    frame_count += 1
    
    # Flip for mirror effect
    frame = cv2.flip(frame, 1)
    
    # Add text
    cv2.putText(frame, f"Frame: {frame_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, "Press 'q' to quit", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
    
    cv2.imshow('Camera Test', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\n✅ Camera test completed successfully!")
        break

cap.release()
cv2.destroyAllWindows()
print("👋 Goodbye!")
