import sys
import cv2

print('Hello OpenCV', cv2.__version__)
img = cv2.imread('ch01/cat.bmp')
if img is None:
    print('There is no image')
    sys.exit()
cv2.namedWindow('image', flags=cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.imwrite('catzz.png',img)
cv2.waitKey()
cv2.destroyAllWindows()
