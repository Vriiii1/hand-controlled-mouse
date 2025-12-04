# 🖐️ Hand-Controlled Mouse

A webcam-based gesture-control system using Python, MediaPipe, and OpenCV.

## 📌 Overview

This project turns your webcam (e.g., iPhone via EpocCam/DroidCam) into a hand-tracking input device that controls:

- **Mouse movement** (hand position)
- **Left click** (pinch gesture)
- **Right click** (fist or two-finger pinch)
- **Scroll** (vertical hand motion or gesture mode)

**Goal**: Create a robust, low-latency gesture-based mouse alternative that works in real time.

## 📦 Tech Stack

- Python 3.9+
- MediaPipe Hands (21 landmarks tracking)
- OpenCV (camera + rendering)
- PyAutoGUI or Pynput (mouse control)
- NumPy for smoothing calculations

## 🎥 Camera Input

You can use your iPhone as a Windows webcam using one of these:
- Elgato EpocCam
- DroidCam
- iVCam

Make sure it appears as a normal webcam (e.g., `VideoCapture(0)`).

## ✋ Gesture Controls

### Cursor Movement
- Track index finger tip landmark (ID 8)
- Map its normalized position → screen coordinates
- Add smoothing (moving average, low-pass filter)

### Left Click — Pinch Gesture
- Detect when thumb tip (ID 4) and index finger tip (ID 8) distance < threshold
- Pinch start → mouseDown
- Pinch end → mouseUp

### Right Click — Fist or Two-Finger Pinch
- Option A: Fist detection (all fingertips close to palm)
- Option B: Middle-finger pinch (ID 12 + ID 4) - More precise

### Scrolling
- Option A: Vertical hand movement (easier initially)
- Option B: Scroll Mode Toggle with pinch + hold

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Vriiii1/hand-controlled-mouse.git
cd hand-controlled-mouse

# Install dependencies
pip install -r requirements.txt
```

## 🎮 Usage

```bash
python hand_mouse.py
```

Press `q` to quit the application.

## 📁 Project Structure

```
handDetection/
│
├── hand_mouse.py          # main script
├── gestures.py            # pinch/fist detection logic
├── smoothing.py           # smoothing filters
├── config.py              # configuration settings
├── README.md              # documentation
├── requirements.txt       # dependencies
├── .gitignore            # git ignore file
└── LICENSE               # project license
```

## 🧠 Smoothing & Stability

To prevent jitter:
- Use a 3–10 frame moving average for finger position
- Ignore hand detections with low confidence
- Add a dead zone (small movements are ignored)

## 🧪 Testing Strategy

1. Start with hand detection debugging window (draw landmarks)
2. Print distances for pinch gestures
3. Add mouse movement but disabled at first (debug mode)
4. When stable → enable real mouse control
5. Tune thresholds for your hand size and camera distance

## 🚀 Future Improvements

- [ ] Add two-hand support
- [ ] Create on-screen UI for mode switching
- [ ] Add gesture for drag & drop
- [ ] Add adaptive sensitivity / acceleration
- [ ] Use Kalman filter for smoother tracking
- [ ] Add configuration file for custom gestures
- [ ] Add gesture recording and playback

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👤 Author

[Vriiii1](https://github.com/Vriiii1)
