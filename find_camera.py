"""
Script to find all available camera indices
"""

import cv2

print("🔍 Searching for available cameras...\n")
print("This may take a moment...\n")

available_cameras = []

# Check indices 0-10
for index in range(11):
    print(f"Checking index {index}...", end=" ")
    cap = cv2.VideoCapture(index)
    
    if cap.isOpened():
        # Try to read a frame to verify it really works
        ret, frame = cap.read()
        if ret:
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            
            print(f"✅ FOUND! Resolution: {width}x{height}, FPS: {fps}")
            available_cameras.append({
                'index': index,
                'width': width,
                'height': height,
                'fps': fps
            })
        else:
            print("⚠️  Opened but cannot read frames")
        cap.release()
    else:
        print("❌ Not available")

print("\n" + "="*60)

if available_cameras:
    print(f"\n✅ Found {len(available_cameras)} camera(s):\n")
    
    for cam in available_cameras:
        print(f"   Index {cam['index']}:")
        print(f"      Resolution: {cam['width']}x{cam['height']}")
        print(f"      FPS: {cam['fps']}")
        print()
    
    print("📝 To use a specific camera, edit config.py:")
    print(f"   CAMERA_INDEX = {available_cameras[0]['index']}  # Change this number\n")
    
    # Test first camera
    first_cam = available_cameras[0]
    print(f"🎥 Opening camera at index {first_cam['index']} for preview...")
    print("   Press 'q' to close preview\n")
    
    cap = cv2.VideoCapture(first_cam['index'])
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        cv2.putText(frame, f"Camera Index: {first_cam['index']}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, "Press 'q' to quit", (10, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        cv2.imshow('Camera Preview', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("\n✅ Preview closed!")
    
else:
    print("\n❌ No cameras found!")
    print("\n💡 Possible reasons:")
    print("   1. No webcam connected")
    print("   2. Camera is being used by another application")
    print("   3. iPhone webcam app (EpocCam/DroidCam) not running")
    print("   4. Camera drivers not installed")
    print("\n📱 If using iPhone as webcam:")
    print("   1. Install EpocCam or DroidCam on both iPhone and PC")
    print("   2. Make sure both are on the same WiFi network")
    print("   3. Start the app on iPhone first, then on PC")
    print("   4. Run this script again")
    print("\n📖 See CAMERA_SETUP.md for detailed instructions")

print("\n" + "="*60 + "\n")
