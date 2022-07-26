import cv2
import numpy as np

path = 'task1_opencv_control/modules/test_frames/2.jpg'
img = cv2.imread(path)

# For stackin the image on one window, we don't need it in our project.
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

# Find the contours and determine the shape
def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 100< area < 39000:
            print(area)
            cv2.drawContours(img_contour, cnt, -1, (0, 128, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            # print(len(approx))
            obj_cor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if obj_cor == 3:
                object_type = "Triangle"
            elif obj_cor == 4:
                asp_ratio = w / float(h)
                if 0.80 < asp_ratio < 1.20:
                    object_type = "Square"
                else:
                    object_type = "Mark"
                    cv2.drawContours(img_contour, cnt, -1, (0, 0, 255), 3)
            elif obj_cor > 4:
                object_type = "Circle"
            else:
                object_type = "None"

            # cv2.rectangle(img_contour, (x,y),(x+h, y+h),(0,0,255),2)
            cv2.putText(img_contour, object_type, (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                        (0, 0, 0), 2)


img_r = resized = cv2.resize(img, (1080, 720), interpolation=cv2.INTER_AREA) #resize the image
imgHSV = cv2.cvtColor(img_r, cv2.COLOR_BGR2HSV) 
img_contour = img_r.copy() 



# To creating mask so only mark and shape are visible #check color_detector.py for determine the value
lower = np.array([0, 143, 31])
upper = np.array([179, 255, 237])
mask = cv2.inRange(imgHSV, lower, upper)
imgResult = cv2.bitwise_and(img_r, img_r, mask=mask)  # converting mask into original color

img_gray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_blur, 25, 25)
#img_dialte = cv2.dilate(img_canny,kernel=np.ones((5,5),np.uint8),iterations=1)


get_contours(img_canny)  # detect images and draw contour

#imgStack = stackImages(0.6, ([img_dialte, img_contour, imgResult],[img, img_gray, img_blur]))

cv2.imshow("Result", img_contour)

# cv2.imshow("Original", img_r)
# cv2.imshow("Gray", img_gray)
# cv2.imshow("blur", img_blur)
cv2.waitKey(0)
