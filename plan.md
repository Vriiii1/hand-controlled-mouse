🖐️ Hand-Controlled Mouse — Project Plan

A webcam-based gesture-control system using Python, MediaPipe, and OpenCV.

📌 1. Project Overview

This project turns your webcam (e.g., iPhone via EpocCam/DroidCam) into a hand-tracking input device that controls:

Mouse movement (hand position)

Left click (pinch gesture)

Right click (fist or two-finger pinch)

Scroll (vertical hand motion or gesture mode)

Goal: Create a robust, low-latency gesture-based mouse alternative that works in real time.

📦 2. Tech Stack

Python 3.9+

MediaPipe Hands (21 landmarks tracking)

OpenCV (camera + rendering)

PyAutoGUI or Pynput (mouse control)

Optional: NumPy for smoothing calculations

🎥 3. Camera Input

You will use your iPhone as a Windows webcam using one of these:

Elgato EpocCam

DroidCam

iVCam

Make sure it appears as a normal webcam (e.g., VideoCapture(0)).

✋ 4. Gesture Controls (Initial Version)
4.1 Cursor Movement

Track index finger tip landmark (ID 8)

Map its normalized position → screen coordinates

Add smoothing (moving average, low-pass filter)

4.2 Left Click — Pinch Gesture

Detect when thumb tip (ID 4) and index finger tip (ID 8) distance < threshold:

Pinch start → mouseDown

Pinch end → mouseUp

4.3 Right Click — Fist or Two-Finger Pinch

Choose one:

Option A: Fist detection

Measure that all fingertips are close to palm landmarks.

Option B: Middle-finger pinch (ID 12 + ID 4)

More precise and less accidental.

4.4 Scrolling

Choose one scrolling scheme:

Option A: Vertical hand movement

Move hand up → scroll up

Move hand down → scroll down

Works only when pinch is not active

Option B: Scroll Mode Toggle

Pinch + hold 1 second → enter scroll mode

Move hand up/down → scroll

Pinch again → exit scroll mode

Option A is easier initially.

🧠 5. Smoothing & Stability

To prevent jitter:

Use a 3–10 frame moving average for finger position

Ignore hand detections with low confidence

Add a dead zone (small movements are ignored)

⚙️ 6. Architecture Overview
[ Webcam / iPhone ] 
        ↓
[ OpenCV frame capture ]
        ↓
[ MediaPipe Hands → 21 landmarks ]
        ↓
[ Gesture Logic ]
    - position → cursor
    - pinch → click
    - fist/pinch2 → right click
    - vertical motion → scroll
        ↓
[ OS Mouse Events (PyAutoGUI/Pynput) ]

🧪 7. Testing Strategy

Start with hand detection debugging window (draw landmarks)

Next, print distances for pinch gestures

Add mouse movement but disabled at first (debug mode)

When stable → enable real mouse control

Tune thresholds for your hand size and camera distance

🚀 8. Future Improvements

Add two-hand support

Create on-screen UI for mode switching

Add gesture for drag & drop

Add adaptive sensitivity / acceleration

Use Kalman filter for smoother tracking

📁 9. File Structure (Suggested)
hand_mouse/
│
├── hand_mouse.py          # main script
├── gestures.py            # pinch/fist detection logic
├── smoothing.py           # smoothing filters
├── README.md              # documentation
└── requirements.txt       # dependencies

📓 10. requirements.txt
opencv-python
mediapipe
pyautogui
numpy

🧩 11. Next Steps

Set up webcam input

Get MediaPipe Hands running

Track index fingertip and draw it (debug view)

Implement cursor movement

Add pinch detection

Add click + scroll logic

Fine-tune thresholds

If you'd like, I can now:

✅ Generate this as a downloadable .md file
✅ Add sample starter code
✅ Add a calibration section
✅ Add illustrations or diagrams

Would you like me to generate the actual .md file now?