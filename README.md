#  Virtual Hand Keyboard

A Python-based virtual keyboard that allows users to type using hand gestures captured through a webcam. The project uses computer vision and hand tracking to detect finger movements and simulate keyboard input without requiring a physical keyboard.

---

## Features

- Real-time hand tracking
- Virtual on-screen keyboard
- Finger position detection
- Pinch gesture to press keys
- Webcam-based interaction
- Simple and beginner-friendly interface

---

##  Technologies Used

- Python 3
- OpenCV
- MediaPipe
- Pynput

---

## Project Structure

```
Virtual-Hand-Keyboard/
│── main.py
│── hand_tracker.py
│── keyboard_ui.py
│── gesture_detector.py
│── requirements.txt
│── README.md
```

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/sec25ec096-boop/Virtual-Hand-Keyboard.git
```

2. Move into the project folder

```bash
cd Virtual-Hand-Keyboard
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Run the project

```bash
python main.py
```

---

## How It Works

1. Open the application.
2. Allow webcam access.
3. Move your index finger over the virtual keyboard.
4. Pinch your thumb and index finger together to select a key.
5. The selected key is typed automatically.

---


---

## Future Improvements

- Voice typing support
- Multiple keyboard layouts
- Better gesture recognition
- Dark mode UI
- Predictive text suggestions

---

## Author

**Prithikasree P**

GitHub: https://github.com/sec25ec096-boop

---

## License

This project is open source and available under the MIT License.
