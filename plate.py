import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

img_ori = cv2.imread('img2.png')
img_ori = cv2.resize(img_ori, [224,224])
h, w, c = img_ori.shape

# plt.figure(figsize=(12,10))
# plt.imshow(img_ori, cmap='gray')
# plt.show()
# print(h,w,c)

gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
# plt.figure(figsize=(12,10))
# plt.imshow(gray)
# plt.show()

# hsv = cv2.cvtColor(img_ori, cv2.COLOR_BGR2HSV)
# gray = hsv[:, :, 2]
# plt.figure(figsize=(12,10))
# plt.imshow(gray)
# plt.show()

img_blurred = cv2.GaussianBlur(img_ori, ksize=(5, 5), sigmaX=0)

img_blur_thresh = cv2.adaptiveThreshold(
    gray,
    maxValue=255.0,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY_INV,
    blockSize=19,
    C=9
)

img_thresh = cv2.adaptiveThreshold(
    gray,
    maxValue=255.0,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY_INV,
    blockSize=19,
    C=9
)

plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.title('Threshold only')
plt.imshow(img_thresh, cmap='gray')
plt.subplot(1,2,2)
plt.title('Blur and Threshold')
plt.imshow(img_blur_thresh, cmap='gray')
plt.show()

contours, _ = cv2.findContours(
    img_blur_thresh,
    mode=cv2.RETR_LIST,
    method=cv2.CHAIN_APPROX_SIMPLE
)

temp_result = np.zeros((h, w, c), dtype=np.uint8)

cv2.drawContours(temp_result, contours=contours, contourIdx=-1,
                 color=(255,255,255))

plt.figure(figsize=(12, 10))
plt.title('temp_result')
plt.imshow(temp_result)
plt.show()