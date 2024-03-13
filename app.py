import cv2
import mediapipe as mp
from controller import Controller
import webbrowser

google_maps_url = 'https://www.google.com/maps'

# Open Google Maps in the default web browser
webbrowser.open(google_maps_url)

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            Controller.hand_Landmarks = handLms
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            Controller.update_fingers_status()
            Controller.cursor_moving()
            Controller.detect_scrolling()
            Controller.detect_zoomming()
            Controller.detect_clicking()
            Controller.detect_dragging()

    cv2.imshow('Hand Tracker', img)
    if cv2.waitKey(5) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
