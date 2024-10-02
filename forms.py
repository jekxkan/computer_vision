import cv2
import numpy as np

kernel = np.ones((5, 5))
def find_form(image):
    """
    Принимает изображение и находит на нем контуры, площадь которых > 1000

    Args:
        image: изображение, переданное в VideoCapture в main
    """
    to_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh1 = 255
    thresh2 = 180
    canny = cv2.Canny(to_gray, thresh1, thresh2)
    dil = cv2.dilate(canny, kernel, iterations= 1)

    contours, _ = cv2.findContours(dil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(image, contour, -1, (200, 200, 0), 3)
