"""
Gesture detection logic for hand landmarks
"""

import math
import config


class GestureDetector:
    """Detects various hand gestures from MediaPipe landmarks"""
    
    def __init__(self):
        self.pinch_threshold = config.PINCH_THRESHOLD
        self.fist_threshold = config.FIST_THRESHOLD
        
    @staticmethod
    def calculate_distance(landmark1, landmark2):
        """Calculate Euclidean distance between two landmarks"""
        return math.sqrt(
            (landmark1.x - landmark2.x) ** 2 +
            (landmark1.y - landmark2.y) ** 2 +
            (landmark1.z - landmark2.z) ** 2
        )
    
    def detect_pinch(self, hand_landmarks):
        """
        Detect pinch gesture (thumb tip to index finger tip)
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            tuple: (is_pinching, distance)
        """
        thumb_tip = hand_landmarks.landmark[4]   # Thumb tip
        index_tip = hand_landmarks.landmark[8]   # Index finger tip
        
        distance = self.calculate_distance(thumb_tip, index_tip)
        is_pinching = distance < self.pinch_threshold
        
        return is_pinching, distance
    
    def detect_two_finger_pinch(self, hand_landmarks):
        """
        Detect two-finger pinch (thumb to middle finger) for right click
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            tuple: (is_pinching, distance)
        """
        thumb_tip = hand_landmarks.landmark[4]    # Thumb tip
        middle_tip = hand_landmarks.landmark[12]  # Middle finger tip
        
        distance = self.calculate_distance(thumb_tip, middle_tip)
        is_pinching = distance < self.pinch_threshold
        
        return is_pinching, distance
    
    def detect_fist(self, hand_landmarks):
        """
        Detect fist gesture (all fingertips close to palm)
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            bool: True if fist is detected
        """
        # Palm base landmark
        palm = hand_landmarks.landmark[0]
        
        # Fingertip landmarks: thumb(4), index(8), middle(12), ring(16), pinky(20)
        fingertips = [4, 8, 12, 16, 20]
        
        # Check if all fingertips are close to palm
        distances = []
        for tip_id in fingertips:
            tip = hand_landmarks.landmark[tip_id]
            distance = self.calculate_distance(palm, tip)
            distances.append(distance)
        
        # Fist detected if average distance is below threshold
        avg_distance = sum(distances) / len(distances)
        is_fist = avg_distance < self.fist_threshold
        
        return is_fist
    
    def get_index_finger_position(self, hand_landmarks):
        """
        Get index finger tip position for cursor control
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            tuple: (x, y, z) normalized coordinates
        """
        index_tip = hand_landmarks.landmark[8]
        return index_tip.x, index_tip.y, index_tip.z
    
    def detect_pointing(self, hand_landmarks):
        """
        Detect pointing gesture (index finger extended, others closed)
        Useful for distinguishing cursor mode from other gestures
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            bool: True if pointing gesture detected
        """
        # Index finger landmarks: MCP(5), PIP(6), DIP(7), TIP(8)
        index_mcp = hand_landmarks.landmark[5]
        index_tip = hand_landmarks.landmark[8]
        
        # Middle finger landmarks
        middle_mcp = hand_landmarks.landmark[9]
        middle_tip = hand_landmarks.landmark[12]
        
        # Index finger should be extended (tip far from MCP)
        index_extended = self.calculate_distance(index_mcp, index_tip) > 0.15
        
        # Middle finger should be bent (tip close to MCP)
        middle_bent = self.calculate_distance(middle_mcp, middle_tip) < 0.12
        
        return index_extended and middle_bent
    
    def get_hand_vertical_position(self, hand_landmarks):
        """
        Get vertical position of hand for scroll detection
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            float: Normalized y-coordinate of palm center
        """
        # Use wrist position as reference
        wrist = hand_landmarks.landmark[0]
        return wrist.y
    
    def detect_scroll_gesture(self, hand_landmarks):
        """
        Detect if hand is in scroll mode (open palm facing camera)
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            bool: True if scroll gesture detected
        """
        # Check if all fingers are extended (open palm)
        fingertips = [8, 12, 16, 20]  # Index, middle, ring, pinky tips
        finger_bases = [5, 9, 13, 17]  # Corresponding MCP joints
        
        extended_count = 0
        for tip_id, base_id in zip(fingertips, finger_bases):
            tip = hand_landmarks.landmark[tip_id]
            base = hand_landmarks.landmark[base_id]
            
            distance = self.calculate_distance(tip, base)
            if distance > 0.15:  # Finger is extended
                extended_count += 1
        
        # Scroll gesture if at least 3 fingers extended
        return extended_count >= 3
