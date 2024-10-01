import cv2
from find_colored_objects import find_red, find_blue, find_green

capture= cv2.VideoCapture(0)

while True:
    return_code, image = capture.read()
    blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
    image_hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

    # #Объединение масок всех цветов
    # combined_mask = red_mask | get_green_mask(image_hsv) | get_blue_mask(image_hsv)
    #
    # # Применение маски для всех цветов к изображению
    # result = cv2.bitwise_and(image, image, mask=mask)

    find_red(image, image_hsv)
    find_green(image, image_hsv)
    find_blue(image, image_hsv)

    cv2.imshow('From camera', image)
    # cv2.imshow('detection', result)

    #Код нажатой клавиши, побитовая операция гарантирует, что код будет соотвествовать ASCII-кодам символов
    key = cv2.waitKey(30) & 0xFF
    #27 номер соответствует клавише "Escape"
    if key == 27:
        break

print(f"Количество красных объектов на последнем кадре: {find_red(image, image_hsv)}")
print(f"Количество зеленых объектов на последнем кадре: {find_green(image, image_hsv)}")
print(f"Количество синих объектов на последнем кадре: {find_blue(image, image_hsv)}")

cv2.destroyAllWindows()

