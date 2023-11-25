import cv2
import os
import numpy as np

# Create a white canvas
canvas = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Define drawing state
drawing = False
ix, iy = -1, -1


# Define mouse callback function
def draw(event, x, y, flags, param):
    global ix, iy, drawing, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(canvas, (ix, iy), (x, y), (0, 0, 0), 1)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(canvas, (ix, iy), (x, y), (0, 0, 0), 1)


# Create a window and set the mouse callback to the draw function
cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", draw)

# Keep the window open until 'q' is pressed
while True:
    cv2.imshow("Canvas", canvas)
    k = cv2.waitKey(1) & 0xFF
    # quit on 'q' key press
    if k == ord("q"):
        break
    file_name = "src/data/files/user_files/drawing.png"
    cv2.imwrite(file_name, canvas)

cv2.destroyAllWindows()
