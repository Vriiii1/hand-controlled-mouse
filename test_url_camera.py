"""
Test DroidCam using direct URL connection instead of virtual camera
"""

import cv2

print("📱 DroidCam Direct URL Connection Test")
print("="*70)
print("\n📋 Instructions:")
print("   1. Open DroidCam app on your iPhone")
print("   2. Note the IP address shown (e.g., 192.168.1.100)")
print("   3. The default port is usually 4747")
print()

# Get IP from user
ip_address = input("Enter the IP address shown in DroidCam app: ").strip()

if not ip_address:
    print("❌ No IP address entered")
    exit(1)

# Try different DroidCam URL formats
urls = [
    f"http://{ip_address}:4747/video",           # Standard DroidCam
    f"http://{ip_address}:4747/mjpegfeed",       # Alternative
    f"http://{ip_address}:4747/cam/1/stream",    # Another format
]

print(f"\n🔍 Testing connection to {ip_address}...\n")

working_url = None

for url in urls:
    print(f"Trying: {url}...", end=" ", flush=True)
    
    cap = cv2.VideoCapture(url)
    
    if cap.isOpened():
        ret, frame = cap.read()
        if ret and frame is not None:
            print("✅ SUCCESS!")
            
            # Save test image
            cv2.imwrite("droidcam_direct.jpg", frame)
            print(f"   Saved test image: droidcam_direct.jpg")
            print(f"   Resolution: {frame.shape[1]}x{frame.shape[0]}")
            
            working_url = url
            cap.release()
            break
        else:
            print("❌ Can't read frames")
    else:
        print("❌ Can't connect")
    
    cap.release()

print("\n" + "="*70)

if working_url:
    print("✅ DroidCam direct connection WORKING!")
    print(f"\n📝 Working URL: {working_url}")
    print("\n📸 Open 'droidcam_direct.jpg' to see the feed")
    print("\n🔧 To use this in the app, we need to modify the code")
    print("   to use this URL instead of camera index.")
    print("\n💡 Would you like me to create a version that uses this URL?")
else:
    print("❌ Could not connect via direct URL")
    print("\n💡 Troubleshooting:")
    print("   • Make sure DroidCam app is running on iPhone")
    print("   • Make sure both devices on same WiFi network")
    print("   • Check the IP address is correct")
    print("   • Try disabling firewall temporarily")
    print("\n🔄 Alternative: Try EpocCam instead")
    print("   EpocCam works better as a standard webcam")

print("="*70)
