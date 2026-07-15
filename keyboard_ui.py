import cv2
import time


# Keyboard Layout

keys = [
    ["1","2","3","4","5","6","7","8","9","0"],
    ["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L"],
    ["Z","X","C","V","B","N","M"],
    ["SPACE","BACKSPACE","ENTER"]
]


# Keyboard settings

KEY_WIDTH = 55
KEY_HEIGHT = 55
GAP = 8

START_X = 80
START_Y = 60


# Store last clicked key

clicked_key = None
click_time = 0


def set_clicked_key(key):
    global clicked_key, click_time

    clicked_key = key
    click_time = time.time()



def draw_round_rectangle(img, start, end, color, thickness=2):

    x1, y1 = start
    x2, y2 = end

    cv2.rectangle(
        img,
        (x1,y1),
        (x2,y2),
        color,
        thickness,
        cv2.LINE_AA
    )



def draw_keyboard(frame, finger=None):

    global clicked_key

    key_positions = []

    for row_index, row in enumerate(keys):

        y = START_Y + row_index * (KEY_HEIGHT + GAP)

        x = START_X


        # Center rows

        if row_index == 2:
            x += 35

        elif row_index == 3:
            x += 90

        elif row_index == 4:
            x += 120



        for key in row:


            width = KEY_WIDTH


            if key == "SPACE":
                width = 220

            elif key == "BACKSPACE":
                width = 150

            elif key == "ENTER":
                width = 120



            color = (255,255,255)


            # Hover detection

            if finger:

                fx, fy = finger

                if (
                    x < fx < x + width
                    and y < fy < y + KEY_HEIGHT
                ):
                    color = (0,255,0)



            # Click animation

            if clicked_key == key:

                if time.time() - click_time < 0.2:
                    color = (255,0,255)

                else:
                    clicked_key = None



            # Draw key

            draw_round_rectangle(
                frame,
                (x,y),
                (x+width,y+KEY_HEIGHT),
                color,
                2
            )


            # Text

            text_size = cv2.getTextSize(
                key,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                2
            )[0]


            text_x = x + (width-text_size[0])//2
            text_y = y + 36


            cv2.putText(
                frame,
                key,
                (text_x,text_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )


            key_positions.append(
                {
                    "key":key,
                    "x":x,
                    "y":y,
                    "w":width,
                    "h":KEY_HEIGHT
                }
            )


            x += width + GAP


    return frame, key_positions