# Configuration Presets

Copy these settings into `config.py` based on your preference:

## Preset 1: ULTRA SMOOTH (Current)
**Best for: Precision work, less jitter**
```python
SMOOTHING_FRAMES = 10
DEAD_ZONE = 8
MOUSE_SPEED_MULTIPLIER = 1.2
MIN_TRACKING_CONFIDENCE = 0.7
alpha = 0.3  # In hand_mouse_no_gui.py
```

## Preset 2: BALANCED
**Best for: General use**
```python
SMOOTHING_FRAMES = 7
DEAD_ZONE = 6
MOUSE_SPEED_MULTIPLIER = 1.3
MIN_TRACKING_CONFIDENCE = 0.6
alpha = 0.4  # In hand_mouse_no_gui.py
```

## Preset 3: RESPONSIVE
**Best for: Fast movements, gaming**
```python
SMOOTHING_FRAMES = 5
DEAD_ZONE = 5
MOUSE_SPEED_MULTIPLIER = 1.5
MIN_TRACKING_CONFIDENCE = 0.5
alpha = 0.5  # In hand_mouse_no_gui.py
```

## Preset 4: FAST & LOOSE
**Best for: Quick navigation, don't mind jitter**
```python
SMOOTHING_FRAMES = 3
DEAD_ZONE = 3
MOUSE_SPEED_MULTIPLIER = 1.8
MIN_TRACKING_CONFIDENCE = 0.4
alpha = 0.6  # In hand_mouse_no_gui.py
```

---

## Individual Parameter Guide

### SMOOTHING_FRAMES
- **Lower (3-5)**: Faster response, more jittery
- **Medium (6-8)**: Balanced
- **Higher (9-12)**: Smoother, slight lag

### DEAD_ZONE
- **Lower (3-5)**: More sensitive, picks up small movements
- **Medium (6-8)**: Balanced
- **Higher (9-15)**: Less jitter, need bigger movements

### MOUSE_SPEED_MULTIPLIER
- **Slower (0.8-1.1)**: Precise control
- **Medium (1.2-1.5)**: Normal speed
- **Faster (1.6-2.0)**: Quick movements

### MIN_TRACKING_CONFIDENCE
- **Lower (0.3-0.5)**: Tracks hand easier, less stable
- **Medium (0.6-0.7)**: Balanced
- **Higher (0.8-0.9)**: Very stable, might lose tracking

### alpha (in hand_mouse_no_gui.py)
- **Lower (0.2-0.3)**: Smoother, more lag
- **Medium (0.4-0.5)**: Balanced
- **Higher (0.6-0.8)**: More responsive, less smooth

---

## Quick Tips

**To make it smoother:**
- Increase SMOOTHING_FRAMES
- Decrease alpha
- Increase MIN_TRACKING_CONFIDENCE
- Increase DEAD_ZONE

**To make it more responsive:**
- Decrease SMOOTHING_FRAMES
- Increase alpha
- Decrease MIN_TRACKING_CONFIDENCE
- Decrease DEAD_ZONE
