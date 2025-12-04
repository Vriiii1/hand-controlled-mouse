"""
Main script for hand-controlled mouse
"""

import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import config
from gestures import GestureDetector
from smoothing import CombinedFilter


class HandMouseController:
    """Main controller for hand-based mouse input"""
    
    def __init__(self):
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=config.MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=config.MIN_TRACKING_CONFIDENCE,
            max_num_hands=config.MAX_NUM_HANDS
        )
        
        # Initialize camera
        self.cap = cv2.VideoCapture(config.CAMERA_INDEX)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)
        
        # Get screen dimensions
        self.screen_width, self.screen_height = pyautogui.size()
        
        # Initialize gesture detector and smoothing filter
        self.gesture_detector = GestureDetector()
        self.position_filter = CombinedFilter(
            window_size=config.SMOOTHING_FRAMES,
            dead_zone=config.DEAD_ZONE,
            alpha=0.5
        )
        
        # State tracking
        self.is_clicking = False
        self.is_right_clicking = False
        self.last_click_time = 0
        self.last_scroll_time = 0
        self.last_scroll_y = None
        
        # FPS calculation
        self.fps_counter = 0
        self.fps_start_time = time.time()
        self.current_fps = 0
        
        # Disable PyAutoGUI failsafe for smooth operation
        pyautogui.FAILSAFE = False
        
        print("🖐️ Hand Mouse Controller initialized")
        print(f"📺 Screen resolution: {self.screen_width}x{self.screen_height}")
        print(f"🎥 Camera resolution: {config.CAMERA_WIDTH}x{config.CAMERA_HEIGHT}")
        print("\nControls:")
        print("  • Move hand to control cursor")
        print("  • Pinch (thumb + index) for left click")
        print("  • Pinch (thumb + middle) for right click")
        print("  • Move hand up/down with open palm to scroll")
        print("  • Press 'q' to quit")
        print("\n" + "="*50)
    
    def calculate_fps(self):
        """Calculate and update FPS"""
        self.fps_counter += 1
        if time.time() - self.fps_start_time > 1:
            self.current_fps = self.fps_counter
            self.fps_counter = 0
            self.fps_start_time = time.time()
    
    def map_to_screen(self, x, y):
        """Map normalized hand coordinates to screen coordinates"""
        # Flip x-coordinate for mirror effect
        screen_x = (1 - x) * self.screen_width
        screen_y = y * self.screen_height
        
        # Apply smoothing
        screen_x, screen_y = self.position_filter.update(screen_x, screen_y)
        
        # Apply speed multiplier
        screen_x *= config.MOUSE_SPEED_MULTIPLIER
        screen_y *= config.MOUSE_SPEED_MULTIPLIER
        
        # Clamp to screen bounds
        screen_x = max(0, min(self.screen_width - 1, screen_x))
        screen_y = max(0, min(self.screen_height - 1, screen_y))
        
        return int(screen_x), int(screen_y)
    
    def handle_left_click(self, is_pinching):
        """Handle left click gesture"""
        current_time = time.time()
        
        if is_pinching and not self.is_clicking:
            # Cooldown check
            if current_time - self.last_click_time > config.CLICK_COOLDOWN:
                pyautogui.mouseDown()
                self.is_clicking = True
                self.last_click_time = current_time
                if config.PRINT_GESTURES:
                    print("🖱️ Left Click DOWN")
        
        elif not is_pinching and self.is_clicking:
            pyautogui.mouseUp()
            self.is_clicking = False
            if config.PRINT_GESTURES:
                print("🖱️ Left Click UP")
    
    def handle_right_click(self, is_pinching):
        """Handle right click gesture"""
        current_time = time.time()
        
        if is_pinching and not self.is_right_clicking:
            # Cooldown check
            if current_time - self.last_click_time > config.CLICK_COOLDOWN:
                pyautogui.rightClick()
                self.is_right_clicking = True
                self.last_click_time = current_time
                if config.PRINT_GESTURES:
                    print("🖱️ Right Click")
        
        elif not is_pinching:
            self.is_right_clicking = False
    
    def handle_scroll(self, hand_landmarks):
        """Handle scroll gesture"""
        current_time = time.time()
        
        if current_time - self.last_scroll_time < config.SCROLL_COOLDOWN:
            return
        
        # Get vertical hand position
        current_y = self.gesture_detector.get_hand_vertical_position(hand_landmarks)
        
        if self.last_scroll_y is not None:
            # Calculate vertical movement
            delta_y = (current_y - self.last_scroll_y) * config.CAMERA_HEIGHT
            
            # Scroll if movement exceeds threshold
            if abs(delta_y) > config.SCROLL_THRESHOLD:
                scroll_amount = -int(delta_y / 10)  # Negative for natural scrolling
                pyautogui.scroll(scroll_amount)
                self.last_scroll_time = current_time
                
                if config.PRINT_GESTURES:
                    print(f"📜 Scroll: {scroll_amount}")
        
        self.last_scroll_y = current_y
    
    def process_frame(self, frame, results):
        """Process a single frame with hand detection results"""
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks if in debug mode
                if config.DEBUG_MODE:
                    self.mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )
                
                # Get index finger position for cursor control
                x, y, z = self.gesture_detector.get_index_finger_position(hand_landmarks)
                screen_x, screen_y = self.map_to_screen(x, y)
                
                # Move cursor
                pyautogui.moveTo(screen_x, screen_y)
                
                # Detect and handle left click (thumb + index pinch)
                is_left_pinching, left_distance = self.gesture_detector.detect_pinch(hand_landmarks)
                self.handle_left_click(is_left_pinching)
                
                # Detect and handle right click (thumb + middle pinch)
                is_right_pinching, right_distance = self.gesture_detector.detect_two_finger_pinch(hand_landmarks)
                self.handle_right_click(is_right_pinching)
                
                # Handle scroll if not clicking
                if not is_left_pinching and not is_right_pinching:
                    if self.gesture_detector.detect_scroll_gesture(hand_landmarks):
                        self.handle_scroll(hand_landmarks)
                else:
                    self.last_scroll_y = None  # Reset scroll position
                
                # Display debug info
                if config.DEBUG_MODE:
                    # Draw cursor position on frame
                    cv2.circle(frame, (int(x * config.CAMERA_WIDTH), int(y * config.CAMERA_HEIGHT)), 
                              10, (0, 255, 0), -1)
                    
                    # Display distances
                    cv2.putText(frame, f"L-Pinch: {left_distance:.3f}", (10, 30),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                    cv2.putText(frame, f"R-Pinch: {right_distance:.3f}", (10, 60),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        return frame
    
    def run(self):
        """Main loop"""
        print("\n🚀 Starting hand mouse controller...")
        print("Show your hand to the camera!\n")
        
        try:
            while True:
                success, frame = self.cap.read()
                if not success:
                    print("❌ Failed to read from camera")
                    break
                
                # Flip frame horizontally for mirror effect
                frame = cv2.flip(frame, 1)
                
                # Convert BGR to RGB for MediaPipe
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Process frame with MediaPipe
                results = self.hands.process(rgb_frame)
                
                # Process detections
                frame = self.process_frame(frame, results)
                
                # Calculate FPS
                self.calculate_fps()
                
                # Display FPS
                if config.SHOW_FPS:
                    cv2.putText(frame, f"FPS: {self.current_fps}", (10, 90),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Show frame if in debug mode
                if config.DEBUG_MODE:
                    cv2.imshow('Hand Mouse Controller', frame)
                
                # Check for quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("\n👋 Quitting...")
                    break
                
        except KeyboardInterrupt:
            print("\n⚠️ Interrupted by user")
        
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Cleanup resources"""
        print("🧹 Cleaning up...")
        self.cap.release()
        cv2.destroyAllWindows()
        self.hands.close()
        print("✅ Cleanup complete")


def main():
    """Entry point"""
    print("\n" + "="*50)
    print("🖐️  HAND-CONTROLLED MOUSE")
    print("="*50 + "\n")
    
    controller = HandMouseController()
    controller.run()


if __name__ == "__main__":
    main()
