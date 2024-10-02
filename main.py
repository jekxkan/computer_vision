import cv2
from find_colored_objects import find_red, find_blue, find_green
from forms import find_form

capture= cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('videos/detected.avi', fourcc, 20.0, (640, 480))
record = False

while True:
    return_code, image = capture.read()
    image = cv2.bilateralFilter(image, 9, 75, 75)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    find_red(image, image_hsv)
    find_green(image, image_hsv)
    find_blue(image, image_hsv)
    find_form(image)

    cv2.imshow('Image', image)

    #Нажать на r, чтобы начать запись
    key_record = cv2.waitKey(1) & 0xFF
    if key_record == ord('r'):
        record = True

    #Нажать на b, чтобы завершить запись
    if key_record == ord('b'):
        record = False
    if record:
        out.write(image)

    #Код нажатой клавиши, побитовая операция гарантирует, что код будет соотвествовать ASCII-кодам символов
    key = cv2.waitKey(30) & 0xFF
    #27 номер соответствует клавише "Escape"
    if key == 27:
        break

print(f"Количество красных объектов на последнем кадре: {find_red(image, image_hsv)}")
print(f"Количество зеленых объектов на последнем кадре: {find_green(image, image_hsv)}")
print(f"Количество синих объектов на последнем кадре: {find_blue(image, image_hsv)}")


if out is not None:
    out.release()
capture.release()
cv2.destroyAllWindows()

