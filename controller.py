import pyautogui
class Controller:
    prev_hand = None
    right_clicked = False
    left_clicked = False
    double_clicked = False
    dragging = False
    hand_Landmarks = None
    little_finger_down = None
    little_finger_up = None
    index_finger_down = None
    index_finger_up = None
    middle_finger_down = None
    middle_finger_up = None
    ring_finger_down = None
    ring_finger_up = None
    Thump_finger_down = None 
    Thump_finger_up = None
    all_fingers_down = None
    all_fingers_up = None
    index_finger_within_Thumb_finger = None
    middle_finger_within_Thumb_finger = None
    little_finger_within_Thumb_finger = None
    ring_finger_within_Thumb_finger = None
    screen_width, screen_height = pyautogui.size()


    @staticmethod
    def lerp(start, end, alpha):
        """Performs linear interpolation between start and end values."""
        return start + (end - start) * alpha


    def update_fingers_status():
        Controller.little_finger_down = Controller.hand_Landmarks.landmark[20].y > Controller.hand_Landmarks.landmark[17].y
        Controller.little_finger_up = Controller.hand_Landmarks.landmark[20].y < Controller.hand_Landmarks.landmark[17].y
        Controller.index_finger_down = Controller.hand_Landmarks.landmark[8].y > Controller.hand_Landmarks.landmark[5].y
        Controller.index_finger_up = Controller.hand_Landmarks.landmark[8].y < Controller.hand_Landmarks.landmark[5].y
        Controller.middle_finger_down = Controller.hand_Landmarks.landmark[12].y > Controller.hand_Landmarks.landmark[9].y
        Controller.middle_finger_up = Controller.hand_Landmarks.landmark[12].y < Controller.hand_Landmarks.landmark[9].y
        Controller.ring_finger_down = Controller.hand_Landmarks.landmark[16].y > Controller.hand_Landmarks.landmark[13].y
        Controller.ring_finger_up = Controller.hand_Landmarks.landmark[16].y < Controller.hand_Landmarks.landmark[13].y
        Controller.Thump_finger_down = Controller.hand_Landmarks.landmark[4].y > Controller.hand_Landmarks.landmark[13].y
        Controller.Thump_finger_up = Controller.hand_Landmarks.landmark[4].y < Controller.hand_Landmarks.landmark[13].y
        Controller.all_fingers_down = Controller.index_finger_down and Controller.middle_finger_down and Controller.ring_finger_down and Controller.little_finger_down
        Controller.all_fingers_up = Controller.index_finger_up and Controller.middle_finger_up and Controller.ring_finger_up and Controller.little_finger_up
        Controller.index_finger_within_Thumb_finger = Controller.hand_Landmarks.landmark[8].y > Controller.hand_Landmarks.landmark[4].y and Controller.hand_Landmarks.landmark[8].y < Controller.hand_Landmarks.landmark[2].y
        Controller.middle_finger_within_Thumb_finger = Controller.hand_Landmarks.landmark[12].y > Controller.hand_Landmarks.landmark[4].y and Controller.hand_Landmarks.landmark[12].y < Controller.hand_Landmarks.landmark[2].y
        Controller.little_finger_within_Thumb_finger = Controller.hand_Landmarks.landmark[20].y > Controller.hand_Landmarks.landmark[4].y and Controller.hand_Landmarks.landmark[20].y < Controller.hand_Landmarks.landmark[2].y
        Controller.ring_finger_within_Thumb_finger = Controller.hand_Landmarks.landmark[16].y > Controller.hand_Landmarks.landmark[4].y and Controller.hand_Landmarks.landmark[16].y < Controller.hand_Landmarks.landmark[2].y
    
    @staticmethod
    def get_position(hand_x_position, hand_y_position):
        """Enhanced with linear interpolation for smooth movements."""
        current_x = int(hand_x_position * Controller.screen_width)
        current_y = int(hand_y_position * Controller.screen_height)

        if Controller.prev_hand is None:
            Controller.prev_hand = (current_x, current_y)

        # Linear interpolation for smooth cursor movement
        new_x = Controller.lerp(Controller.prev_hand[0], current_x, 0.3) # Adjust alpha for smoother movements
        new_y = Controller.lerp(Controller.prev_hand[1], current_y, 0.3)

        Controller.prev_hand = (new_x, new_y)

        return new_x, new_y
        
    @staticmethod
    def cursor_moving():
        # Assumes hand_Landmarks has been updated
        if Controller.hand_Landmarks:
            # Using the index finger tip position for cursor movement
            fingertip_x = Controller.hand_Landmarks.landmark[8].x
            fingertip_y = Controller.hand_Landmarks.landmark[8].y
            x, y = Controller.get_position(fingertip_x, fingertip_y)
            pyautogui.moveTo(x, y, duration=0.01)
    
    def detect_scrolling():
        scrolling_up =  Controller.little_finger_up and Controller.index_finger_down and Controller.middle_finger_down and Controller.ring_finger_down
        if scrolling_up:
            pyautogui.scroll(120)
            print("Scrolling UP")

        scrolling_down = Controller.index_finger_up and Controller.middle_finger_down and Controller.ring_finger_down and Controller.little_finger_down
        if scrolling_down:
            pyautogui.scroll(-120)
            print("Scrolling DOWN")
    

    def detect_zoomming():
        zoomming = Controller.index_finger_up and Controller.middle_finger_up and Controller.ring_finger_down and Controller.little_finger_down
        window = .05
        index_touches_middle = abs(Controller.hand_Landmarks.landmark[8].x - Controller.hand_Landmarks.landmark[12].x) <= window
        zoomming_out = zoomming and index_touches_middle
        zoomming_in = zoomming and not index_touches_middle
        
        if zoomming_out:
            pyautogui.keyDown('ctrl')
            pyautogui.scroll(-6)
            pyautogui.keyUp('ctrl')
            print("Zooming Out")

        if zoomming_in:
            pyautogui.keyDown('ctrl')
            pyautogui.scroll(6)
            pyautogui.keyUp('ctrl')
            print("Zooming In")

    def detect_clicking():
        left_click_condition = Controller.index_finger_within_Thumb_finger and Controller.middle_finger_up and Controller.ring_finger_up and Controller.little_finger_up and not Controller.middle_finger_within_Thumb_finger and not Controller.ring_finger_within_Thumb_finger and not Controller.little_finger_within_Thumb_finger
        if not Controller.left_clicked and left_click_condition:
            pyautogui.click()
            Controller.left_clicked = True
            print("Left Clicking")
        elif not Controller.index_finger_within_Thumb_finger:
            Controller.left_clicked = False

        right_click_condition = Controller.middle_finger_within_Thumb_finger and Controller.index_finger_up and Controller.ring_finger_up and Controller.little_finger_up and not Controller.index_finger_within_Thumb_finger and not Controller.ring_finger_within_Thumb_finger and not Controller.little_finger_within_Thumb_finger
        if not Controller.right_clicked and right_click_condition:
            pyautogui.rightClick()
            Controller.right_clicked = True
            print("Right Clicking")
        elif not Controller.middle_finger_within_Thumb_finger:
            Controller.right_clicked = False

        double_click_condition = Controller.ring_finger_within_Thumb_finger and Controller.index_finger_up and Controller.middle_finger_up and Controller.little_finger_up and not Controller.index_finger_within_Thumb_finger and not Controller.middle_finger_within_Thumb_finger and not Controller.little_finger_within_Thumb_finger
        if not Controller.double_clicked and  double_click_condition:
            pyautogui.doubleClick()
            Controller.double_clicked = True
            print("Double Clicking")
        elif not Controller.ring_finger_within_Thumb_finger:
            Controller.double_clicked = False
    
    def detect_dragging():
        if not Controller.dragging and Controller.all_fingers_down:
            pyautogui.mouseDown(button = "left")
            Controller.dragging = True
            print("Dragging")
        elif not Controller.all_fingers_down:
            pyautogui.mouseUp(button = "left")
            Controller.dragging = False