import math


class GestureDetector:

    def is_pinch(self, landmarks):

        if len(landmarks) < 9:
            return False

        _, tx, ty = landmarks[4]
        _, ix, iy = landmarks[8]

        distance = math.hypot(tx - ix, ty - iy)

        return distance < 60