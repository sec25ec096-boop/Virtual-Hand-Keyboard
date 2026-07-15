import cv2
import time

try:
    from pynput.keyboard import Controller, Key
except ImportError:
    Controller = None
    class Key:
        space = " "
        enter = "\n"
        backspace = "BACKSPACE"

from hand_tracker import HandTracker
from keyboard_ui import draw_keyboard, set_clicked_key
from gesture_detector import GestureDetector


keyboard = Controller() if Controller else None

typed_text = ""


def get_pressed_key(finger, key_positions):

    if finger is None:
        return None

    fx, fy = finger

    for key in key_positions:

        if (
            key["x"] < fx < key["x"] + key["w"]
            and key["y"] < fy < key["y"] + key["h"]
        ):
            return key["key"]

    return None



def type_key(key):

    global typed_text


    if key == "SPACE":

        keyboard.press(Key.space)
        keyboard.release(Key.space)

        typed_text += " "



    elif key == "ENTER":

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        typed_text += "\n"



    elif key == "BACKSPACE":

        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)

        typed_text = typed_text[:-1]



    else:

        keyboard.press(key.lower())
        keyboard.release(key.lower())

        typed_text += key



def draw_text_box(frame):

    cv2.rectangle(
        frame,
        (50, 5),
        (900, 50),
        (255,255,255),
        2
    )


    cv2.putText(
        frame,
        typed_text[-40:],
        (70,35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )



def main():

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)


    if not cap.isOpened():

        print("Camera error")
        return



    cv2.namedWindow(
        "AI Virtual Keyboard",
        cv2.WINDOW_NORMAL
    )

    cv2.resizeWindow(
        "AI Virtual Keyboard",
        1280,
        720
    )



    tracker = HandTracker()
    gesture = GestureDetector()


    last_press = 0



    while True:


        success, frame = cap.read()


        if not success:
            break



        frame = cv2.flip(frame,1)



        frame, landmarks = tracker.find_hands(frame)



        finger = None


        if len(landmarks)>8:


            _,x,y = landmarks[8]

            finger=(x,y)


            cv2.circle(
                frame,
                (x,y),
                10,
                (255,0,255),
                -1
            )



        draw_text_box(frame)



        frame,key_positions = draw_keyboard(
            frame,
            finger
        )



        if finger and gesture.is_pinch(landmarks):


            current=time.time()


            if current-last_press>0.45:


                key=get_pressed_key(
                    finger,
                    key_positions
                )


                if key:

                    print("Pressed:",key)

                    type_key(key)

                    set_clicked_key(key)



                last_press=current




        cv2.imshow(
            "AI Virtual Keyboard",
            frame
        )



        if cv2.waitKey(1)&0xFF==ord("q"):

            break



    cap.release()
    cv2.destroyAllWindows()



if __name__=="__main__":

    main()