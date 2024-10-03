import numpy as np
import cv2

def find_red(image, image_hsv) -> int:
    """
    Устанавливает пороги для красного цвета, выделяет контуры красных объектов,
    "упаковывает" в прямоугольник и подписывает

    Args:
        image: изображение, переданное в VideoCapture в main
        image_hsv: изображение, переданное в VideoCapture в main, в цветовом формате HSV

    Returns:
        count_red(int): количество красный объектов
    """
    # Установка порогов для красного цвета
    lower_red = np.array([0, 130, 145])
    upper_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(image_hsv, lower_red, upper_red)

    # Выделение контуров, "упаковка" в прямоугольник и соответвутствующая подпись для красных объектов
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel=kernel)

    red_contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    red_contours = sorted(red_contours, key=cv2.contourArea, reverse=True)

    for x in range(len(red_contours)):
        area = cv2.contourArea(red_contours[x])
        if area > 100:
            x, y, width, height = cv2.boundingRect(red_contours[x])
            print("Найден красный объект")
            image = cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
            image_red = cv2.rectangle(image, (x, y), (x + 60, y - 25), (0, 0, 0), -1)
            cv2.putText(image_red, 'RED', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    count_red = len(red_contours)

    return count_red

def find_green(image, image_hsv) -> int:
    """
    Устанавливает пороги для зеленого цвета, выделяет контуры зеленых объектов,
    "упаковывает" в прямоугольник и подписывает

    Args:
        image: изображение, переданное в VideoCapture в main
        image_hsv: изображение, переданное в VideoCapture в main, в цветовом формате HSV

    Returns:
        count_green(int): количество зеленых объектов
    """
    # Установка порогов для зеленого цвета
    lower_green = np.array([50, 60, 60])
    upper_green = np.array([90, 255, 255])
    green_mask = cv2.inRange(image_hsv, lower_green, upper_green)

    # Выделение контуров, "упаковка" в прямоугольник и соответвутствующая подпись для зеленых объектов
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel=kernel)

    green_contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    green_contours = sorted(green_contours, key=cv2.contourArea, reverse=True)

    for x in range(len(green_contours)):
        area = cv2.contourArea(green_contours[x])
        if area > 100:
            print("Найден зеленый объект")
            x, y, width, height = cv2.boundingRect(green_contours[x])

            image = cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
            image_red = cv2.rectangle(image, (x, y), (x + 100, y - 25), (0, 0, 0), -1)
            cv2.putText(image_red, 'GREEN', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    count_green = len(green_contours)

    return count_green

def find_blue(image, image_hsv) -> int:
    """
    Устанавливает пороги для синего цвета, выделяет контуры синих объектов,
    "упаковывает" в прямоугольник и подписывает

    Args:
        image: изображение, переданное в VideoCapture в main
        image_hsv: изображение, переданное в VideoCapture в main, в цветовом формате HSV

    Returns:
        count_blue(int): количество синих объектов
    """
    # Установка порогов для синего цвета
    lower_blue = np.array([100, 50, 0])
    upper_blue = np.array([150, 255, 255])
    blue_mask = cv2.inRange(image_hsv, lower_blue, upper_blue)

    # Выделение контуров, "упаковка" в прямоугольник и соответвутствующая подпись для синих объектов
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel=kernel)

    blue_contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    blue_contours = sorted(blue_contours, key=cv2.contourArea, reverse=True)

    for x in range(len(blue_contours)):
        area = cv2.contourArea(blue_contours[x])
        if area > 100:
            x, y, width, height = cv2.boundingRect(blue_contours[x])
            print("Найден синий объект")
            image = cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
            image_red = cv2.rectangle(image, (x, y), (x + 80, y - 25), (0, 0, 0), -1)
            cv2.putText(image_red, 'BLUE', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    count_blue = len(blue_contours)

    return count_blue

