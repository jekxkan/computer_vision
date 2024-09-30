import cv2
import numpy as np

capture= cv2.VideoCapture(0)

while True:
    return_code, image = capture.read()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blurred_img = cv2.GaussianBlur(image, (5, 5), 0)

    #Установка порогов для красного цвета
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(image_hsv, lower_red, upper_red)

    # Установка порогов для синего цвета
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([120, 255, 255])
    blue_mask = cv2.inRange(image_hsv, lower_blue, upper_blue)

    # Установка порогов для зеленого цвета
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])
    green_mask = cv2.inRange(image_hsv, lower_green, upper_green)

    # Объединение масок всех цветов
    combined_mask = red_mask | blue_mask | green_mask

    # Применение маски к заблюренному изображению
    result = cv2.bitwise_and(blurred_img, blurred_img, mask=combined_mask)


    cv2.imshow('From camera', blurred_img)
    cv2.imshow('detection_colors', result)

    #Код нажатой клавиши, побитовая операция гарантирует, что код будет соотвествовать ASCII-кодам символов
    key = cv2.waitKey(30) & 0xFF
    #27 номер соответствует клавише "Escape"
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()

