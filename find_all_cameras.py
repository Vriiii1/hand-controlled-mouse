"""
Find ALL available cameras including virtual cameras
"""

import cv2

print("🔍 Searching ALL camera indices (0-20)...")
print("This will take about 30 seconds...\n")

available = []

for i in range(21):
    print(f"Testing index {i}...", end=" ", flush=True)
    
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # Use DirectShow on Windows
    
    if cap.isOpened():
        ret, frame = cap.read()
        if ret and frame is not None:
            h, w = frame.shape[:2]
            
            # Check if it's a real camera (not just a virtual placeholder)
            if h > 0 and w > 0:
                print(f"✅ FOUND! {w}x{h}")
                
                # Save a test image
                filename = f"camera_index_{i}.jpg"
                cv2.imwrite(filename, frame)
                
                available.append({
                    'index': i,
                    'width': w,
                    'height': h,
                    'file': filename
                })
            else:
                print("⚠️  Opened but invalid dimensions")
        else:
            print("⚠️  Opened but can't read frames")
        cap.release()
    else:
        print("❌")

print("\n" + "="*70)
print(f"\n✅ Found {len(available)} working camera(s):\n")

for cam in available:
    print(f"   Camera Index {cam['index']}:")
    print(f"      Resolution: {cam['width']}x{cam['height']}")
    print(f"      Test image: {cam['file']} (OPEN THIS!)")
    print()

if available:
    print("📋 Next steps:")
    print("   1. Open each test image file")
    print("   2. Find which one shows your DroidCam feed")
    print("   3. Update config.py with that camera index")
    print(f"\n   Example: If camera_index_3.jpg shows your feed,")
    print("   then edit config.py and set: CAMERA_INDEX = 3")
else:
    print("❌ No cameras found!")
    print("\n💡 Troubleshooting:")
    print("   1. Make sure DroidCam Client is running on PC")
    print("   2. Click 'Start' in DroidCam Client")
    print("   3. Close OBS Studio if it's running")
    print("   4. Restart DroidCam Client")
    print("   5. Run this script again")

print("\n" + "="*70)
