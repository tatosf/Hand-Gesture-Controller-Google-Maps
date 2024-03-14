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

## How to Run
After installing the required libraries, run the app.py file in a Python environment that has access to a webcam. Upon execution, the program will automatically open Google Maps in your default web browser and start capturing video from the webcam. You can then control Google Maps using the following hand gestures:

  - **Cursor moving**: Raise all fingers together and move your hand to move the cursor and control it.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Mouse_moving](https://user-images.githubusercontent.com/129029089/227950094-4dae7a2d-a332-41ad-aa13-a186a5052f60.png)

  - **Cursor freezing**: Close your thumb and Raise all other fingers together freeze the cursor and prevent it from moving.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Mouse_freezing](https://user-images.githubusercontent.com/129029089/227953353-6cb5bfe7-8beb-43df-a4a7-988f43e51c94.png)

  - **Drag and drop**: Close your hand into a fist and move it around to drag and drop objects.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Drag](https://user-images.githubusercontent.com/129029089/227953920-2049922f-d76d-4a3b-b132-d6ff9f234d1e.png)

  - **Right-click**: Raise your index finger while keeping the other fingers closed.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Right_click](https://user-images.githubusercontent.com/129029089/227954273-7184fe9b-39b5-4bfc-bc49-2cc9b17f18c7.png)

  - **Left-click**: Raise your middle finger while keeping the other fingers closed.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Left_click](https://user-images.githubusercontent.com/129029089/227954145-e8915010-4a4d-46b1-9e24-5a4c48637b51.png)

  - **Double-click**: Raise your index and middle finger while keeping the other fingers closed.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Double_click](https://user-images.githubusercontent.com/129029089/227954025-6ea2c2bc-4f49-450c-ad50-1d2400a33ea8.png)

  - **Scroll up**: Move your index and middle finger towards the screen.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Scrolling_up](https://user-images.githubusercontent.com/129029089/227954370-66157650-1e08-425f-940e-1f35517fd92a.png)

  - **Scroll down**: Move your index and middle finger away from the screen.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Scrolling_down](https://user-images.githubusercontent.com/129029089/227954424-f6d67430-601f-4238-ab74-7247f8471c6a.png)

  - **Zoom in**: Pinch your index finger and thumb together.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Zooming_in](https://user-images.githubusercontent.com/129029089/227954523-286c4c7f-33d5-4ea1-850e-8355021da51d.png)

  - **Zoom out**: Spread your index finger and thumb apart.<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp; ![Zooming_out](https://user-images.githubusercontent.com/129029089/227954586-4774546f-2611-482a-a722-52339ab57bb5.png)


## How it Works
The program utilizes the Mediapipe library to detect hand landmarks from the video captured by the webcam. The detected hand landmarks are then processed by controller.py, which maps these landmarks to specific actions for controlling Google Maps, such as cursor movement, clicking, scrolling, and zooming.

## Limitations

Currently, the program supports controlling Google Maps with gestures from a single hand and may encounter difficulties in low-light conditions. Future updates may include multi-hand gesture support and improved light condition handling.

