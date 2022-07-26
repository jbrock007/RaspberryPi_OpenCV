from ctypes import sizeof
import logging
import threading
import cv2
import numpy as np

USE_FAKE_PI_CAMERA = True  # Chage to FALSE if testing in the Raspberry Pi

if USE_FAKE_PI_CAMERA:
    from .camera import Camera  # For running app
else:
    from .pi_camera import Camera  # For running Raspberry Pi

log = logging.getLogger(
    __name__)  # Creates a logger instance, we use it to log things out


class OpenCVController(object):

    def __init__(self):
        self.current_shape = [False, False, False]
        self.camera = Camera()
        print('OpenCV controller initiated')

    def process_frame(self):
        frame = self.camera.get_frame()
        print(type(frame))
        #-----------------'added code------------------#
        jpg_as_np = np.frombuffer(frame, np.uint8)  # fromstring
        img = cv2.imdecode(jpg_as_np, cv2.COLOR_RGB2BGR)
        # resized = cv2.resize(img, (720,480), interpolation = cv2.INTER_AREA)

        # print(type(resized))

        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_contour = img.copy()
        # To creating mask so only mark and shape are visible #check color_detector.py for determine the value
        lower = np.array([0, 122, 31])
        upper = np.array([179, 255, 237])
        mask = cv2.inRange(imgHSV, lower, upper)
        # converting mask into original color
        imgResult = cv2.bitwise_and(img, img, mask=mask)

        img_gray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
        img_canny = cv2.Canny(img_blur, 25, 25)
        img_dialte = cv2.dilate(img_canny, kernel=np.ones(
            (2, 2), np.uint8), iterations=1)

        contours, hierarchy = cv2.findContours(
            img_dialte, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if 1600 < area < 303000:
                print(area)
                cv2.drawContours(img_contour, cnt, -1, (0, 128, 0), 8)
                peri = cv2.arcLength(cnt, True)
                # print(peri)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                # print(len(approx))
                obj_cor = len(approx)
                print(obj_cor)
                x, y, w, h = cv2.boundingRect(approx)

                if obj_cor == 3 and area > 90000:
                    object_type = "Triangle"
                elif obj_cor == 4 and area > 150000:
                    asp_ratio = w / float(h)
                    if 0.85 < asp_ratio < 1.15:
                        object_type = "Square"
                    else:
                        object_type = "Mark"
                        cv2.drawContours(img_contour, cnt, -1, (0, 0, 255), 8)
                elif obj_cor > 4 and area > 150000:
                    object_type = "Circle"
                else:

                    object_type = "None"
                # cv2.rectangle(img_contour, (x,y),(x+h, y+h),(0,0,255),2)

                    object_type = " "

                # cv2.rectangle(img_contour, (x,y),(x+w, y+h),(0,0,121),2)

                cv2.putText(img_contour, object_type, (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 2,
                            (0, 0, 0), 7)

        ret, output = cv2.imencode('.jpg', img_contour)

        #---------------'added code'---------------------#
        print('Monitoring')
        return output.tobytes()

    def get_current_shape(self):
         frame = self.camera.get_frame()
         jpg_as_np = np.frombuffer(frame, np.uint8)  # fromstring
         img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
         return self.current_shape
