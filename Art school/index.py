import cv2
import numpy as np
import time
canvas = None
drawing = False
start_x, start_y = -1, -1

def draw(event, x, y, flags, param):
    global canvas, drawing, start_x, start_y

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(canvas, (start_x, start_y), (x, y), (0, 0, 255), 2)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (start_x, start_y), (x, y), (0, 0, 255), 2)
            start_x, start_y = x, y

canvas = 255 * np.ones((500, 500, 3), dtype=np.uint8)  # Beyaz bir tuval oluşturuyoruz

cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw)

while True:
    cv2.imshow('Canvas', canvas)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # 'q' tuşuna basarak programı sonlandırıyoruz
        break

cv2.destroyAllWindows()

print('Wow thats excellent drawing')
time.sleep(1)
print('But we dont accept you our school')
time.sleep(1)
print('-NEIN...')