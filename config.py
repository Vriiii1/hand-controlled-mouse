"""
Configuration settings for hand-controlled mouse
"""

# Camera settings
CAMERA_INDEX = 1  # DroidCam found at index 1
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# MediaPipe settings
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.5
MAX_NUM_HANDS = 1  # Start with one hand for simplicity

# Screen settings (will be auto-detected)
SCREEN_WIDTH = None  # Auto-detected at runtime
SCREEN_HEIGHT = None  # Auto-detected at runtime

# Gesture detection thresholds
PINCH_THRESHOLD = 0.05  # Distance threshold for pinch detection (normalized)
FIST_THRESHOLD = 0.1    # Distance threshold for fist detection
SCROLL_THRESHOLD = 30   # Pixel movement threshold for scroll activation

# Smoothing settings
SMOOTHING_FRAMES = 5    # Number of frames to average for position smoothing
DEAD_ZONE = 5           # Minimum pixel movement to register

# Mouse control settings
MOUSE_SPEED_MULTIPLIER = 1.5  # Cursor movement speed
SCROLL_SPEED = 20             # Scroll speed in pixels

# Debug settings
DEBUG_MODE = True       # Show debug window with landmarks
SHOW_FPS = True        # Display FPS counter
PRINT_GESTURES = True  # Print detected gestures to console

# Gesture cooldowns (in seconds)
CLICK_COOLDOWN = 0.3    # Minimum time between clicks
SCROLL_COOLDOWN = 0.1   # Minimum time between scroll events
