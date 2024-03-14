# Hand Gesture Recognition for Google Maps Control

This Python project enables controlling Google Maps through hand gestures, offering an intuitive way to interact with maps without using traditional input devices. The program recognizes hand gestures through a webcam using the Mediapipe library and translates these gestures into mouse actions with the PyAutoGUI library, allowing for seamless navigation and control of Google Maps in a web browser.

## Project Structure

The project comprises two main files:

- `app.py`: Contains the main program logic, initializing hand gesture recognition and opening Google Maps in a default web browser.
- `controller.py`: Responsible for interpreting hand gestures and executing corresponding mouse cursor movements and clicks to control Google Maps.

An additional file, `requirements.txt`, is provided to facilitate the installation of necessary libraries.

## Requirements

To run the program, ensure you have the following libraries installed:

- OpenCV
- Mediapipe
- PyAutoGUI

You can install these libraries using pip:

```bash
pip install -r requirements.txt
```

## How to Run
After installing the required libraries, run the app.py file in a Python environment that has access to a webcam. Upon execution, the program will automatically open Google Maps in your default web browser and start capturing video from the webcam. You can then control Google Maps using the following hand gestures:

  - **Cursor moving**: Raise all fingers together and move your hand to move the cursor and control it.  
  ![Mouse_moving](gestures/Mouse_moving.png)

- **Cursor freezing**: Close your thumb and Raise all other fingers together freeze the cursor and prevent it from moving.  
  ![Mouse_freezing](gestures/Mouse_freezing.png)

- **Drag and drop**: Close your hand into a fist and move it around to drag and drop objects.  
  ![Drag](gestures/Drag.png) gestures/Drag.png

- **Right-click**: Raise your index finger while keeping the other fingers closed.  
  ![Right_click](gestures/Right_click.png)

- **Left-click**: Raise your middle finger while keeping the other fingers closed.  
  ![Left_click](gestures/Left_click.png)

- **Double-click**: Raise your index and middle finger while keeping the other fingers closed.  
  ![Double_click](gestures/Double_click.png)

- **Scroll up**: Move your index and middle finger towards the screen.  
  ![Scrolling_up](gestures/Scrolling_up.png)

- **Scroll down**: Move your index and middle finger away from the screen.  
  ![Scrolling_down](gestures/Scrolling_down.png)

- **Zoom in**: Pinch your index finger and thumb together.  
  ![Zooming_in](gestures/Zooming_in.png)

- **Zoom out**: Spread your index finger and thumb apart.  
  ![Zooming_out](gestures/Zooming_out.png)


## How it Works
The program utilizes the Mediapipe library to detect hand landmarks from the video captured by the webcam. The detected hand landmarks are then processed by controller.py, which maps these landmarks to specific actions for controlling Google Maps, such as cursor movement, clicking, scrolling, and zooming.

## Limitations

Currently, the program supports controlling Google Maps with gestures from a single hand and may encounter difficulties in low-light conditions. Future updates may include multi-hand gesture support and improved light condition handling.

