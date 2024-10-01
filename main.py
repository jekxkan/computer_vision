import cv2
import numpy as np

def nothing(x):
    pass

capture= cv2.VideoCapture(0)
# cv2.namedWindow('frame')
# cv2.createTrackbar('H', 'frame', 0,180, nothing)
# cv2.createTrackbar('S', 'frame', 0,255, nothing)
# cv2.createTrackbar('V', 'frame', 0,255, nothing)
#
# cv2.createTrackbar('HL', 'frame', 0,180, nothing)
# cv2.createTrackbar('SL', 'frame', 0,255, nothing)
# cv2.createTrackbar('VL', 'frame', 0,255, nothing)

while True:
    return_code, image = capture.read()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blurred_image = cv2.GaussianBlur(image, (3, 3), 0)

    # h = cv2.getTrackbarPos('H', 'frame')
    # s = cv2.getTrackbarPos('S', 'frame')
    # v = cv2.getTrackbarPos('V', 'frame')
    #
    # hl = cv2.getTrackbarPos('HL', 'frame')
    # sl = cv2.getTrackbarPos('SL', 'frame')
    # vl = cv2.getTrackbarPos('VL', 'frame')
    #
    # lower = np.array([hl, sl, vl])
    # upper = np.array([h, s, v])
    # mask = cv2.inRange(image_hsv, lower, upper)

    # Установка порогов для синего цвета
    lower_blue = np.array([110, 30, 115])
    upper_blue = np.array([130, 255, 255])
    blue_mask = cv2.inRange(image_hsv, lower_blue, upper_blue)

    # Установка порогов для зеленого цвета
    lower_green = np.array([50, 60, 60])
    upper_green = np.array([90, 255, 255])
    green_mask = cv2.inRange(image_hsv, lower_green, upper_green)

    # Установка порогов для красного цвета
    lower_red = np.array([0, 100, 155])
    upper_red = np.array([60, 255, 255])
    red_mask = cv2.inRange(image_hsv, lower_red, upper_red)

    # Объединение масок всех цветов
    combined_mask = red_mask | blue_mask | green_mask

    # Применение маски к заблюренному изображению
    result = cv2.bitwise_and(image, image, mask=combined_mask)
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel=kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel=kernel)

    contours, _ = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)

    for x in range(len(contours)):
        area = cv2.contourArea(contours[x])
        if area > 100:
            x, y, width, height = cv2.boundingRect(contours[x])
            image_blue = cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
            image_blue = cv2.rectangle(image_blue, (x, y), (x + 60, y - 25), (0, 0 ,0), -1)
            cv2.putText(image_blue, 'BLUE', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0,(255, 255, 255), 2)

            image_red = cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
            image_red = cv2.rectangle(image_red, (x, y), (x + 60, y - 25), (0, 0, 0), -1)
            cv2.putText(image, 'RED', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

            image_green = cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
            image_green = cv2.rectangle(image_green, (x, y), (x + 60, y - 25), (0, 0, 0), -1)
            #cv2.putText(image_green, 'GREEN', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)


    cv2.imshow('opening', image)
    cv2.imshow('result', closing)


    #Код нажатой клавиши, побитовая операция гарантирует, что код будет соотвествовать ASCII-кодам символов
    key = cv2.waitKey(30) & 0xFF
    #27 номер соответствует клавише "Escape"
    if key == 27:
        break

cv2.destroyAllWindows()

