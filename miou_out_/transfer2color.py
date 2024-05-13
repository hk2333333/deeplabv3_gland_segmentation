import cv2

# 读取灰度图
gray_img = cv2.imread('detection-results/testB_4.png', cv2.IMREAD_GRAYSCALE)

for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        if gray_img[i][j] >  0:
            gray_img[i][j] = 255

cv2.imshow('colored', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


