"""
Smoothing filters for hand tracking data
"""

import numpy as np
from collections import deque


class MovingAverageFilter:
    """Simple moving average filter for position smoothing"""
    
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.x_history = deque(maxlen=window_size)
        self.y_history = deque(maxlen=window_size)
    
    def update(self, x, y):
        """Add new position and return smoothed position"""
        self.x_history.append(x)
        self.y_history.append(y)
        
        smooth_x = sum(self.x_history) / len(self.x_history)
        smooth_y = sum(self.y_history) / len(self.y_history)
        
        return smooth_x, smooth_y
    
    def reset(self):
        """Clear history"""
        self.x_history.clear()
        self.y_history.clear()


class ExponentialFilter:
    """Exponential smoothing filter (more responsive than moving average)"""
    
    def __init__(self, alpha=0.5):
        """
        Args:
            alpha: Smoothing factor (0-1). Higher = more responsive, lower = smoother
        """
        self.alpha = alpha
        self.prev_x = None
        self.prev_y = None
    
    def update(self, x, y):
        """Apply exponential smoothing"""
        if self.prev_x is None:
            self.prev_x = x
            self.prev_y = y
            return x, y
        
        smooth_x = self.alpha * x + (1 - self.alpha) * self.prev_x
        smooth_y = self.alpha * y + (1 - self.alpha) * self.prev_y
        
        self.prev_x = smooth_x
        self.prev_y = smooth_y
        
        return smooth_x, smooth_y
    
    def reset(self):
        """Reset filter state"""
        self.prev_x = None
        self.prev_y = None


class DeadZoneFilter:
    """Filter out small movements below a threshold"""
    
    def __init__(self, threshold=5):
        """
        Args:
            threshold: Minimum pixel distance to register movement
        """
        self.threshold = threshold
        self.last_x = None
        self.last_y = None
    
    def update(self, x, y):
        """Only return new position if movement exceeds threshold"""
        if self.last_x is None:
            self.last_x = x
            self.last_y = y
            return x, y
        
        distance = np.sqrt((x - self.last_x)**2 + (y - self.last_y)**2)
        
        if distance > self.threshold:
            self.last_x = x
            self.last_y = y
            return x, y
        
        return self.last_x, self.last_y
    
    def reset(self):
        """Reset filter state"""
        self.last_x = None
        self.last_y = None


class CombinedFilter:
    """Combines multiple filters for optimal smoothing"""
    
    def __init__(self, window_size=5, dead_zone=5, alpha=0.5):
        self.moving_avg = MovingAverageFilter(window_size)
        self.dead_zone = DeadZoneFilter(dead_zone)
        self.exponential = ExponentialFilter(alpha)
    
    def update(self, x, y):
        """Apply all filters in sequence"""
        # First apply exponential smoothing for responsiveness
        x, y = self.exponential.update(x, y)
        
        # Then apply moving average for additional smoothing
        x, y = self.moving_avg.update(x, y)
        
        # Finally apply dead zone to eliminate jitter
        x, y = self.dead_zone.update(x, y)
        
        return x, y
    
    def reset(self):
        """Reset all filters"""
        self.moving_avg.reset()
        self.dead_zone.reset()
        self.exponential.reset()
