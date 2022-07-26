from modules.opencv_controller import OpenCVController
import time
import cv2
import numpy as np
import base64

# Do NOT change this script
opencv_controller = OpenCVController()

for i in range(6):
    print("----------- Distance number: ", i)
    frame,obj_list = opencv_controller.process_frame()
    jpg_as_np = np.frombuffer(frame, np.uint8) #fromstring
    img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
    
    cv2.imshow('image', img) # Not in Raspberry Piw

    print("Current shape from OpenCV: ", opencv_controller.get_current_shape())
    print("---------------------------------")

    cv2.waitKey(0) # Not in Raspberry Pi
    cv2.destroyAllWindows() # Not in Raspberry Pi
