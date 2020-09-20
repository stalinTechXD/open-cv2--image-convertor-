import cv2 

img = cv2.imread('rayan.jpg')
gray = cv2.imread('rayan.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow(' gray pic' , gray)
cv2.imshow('profile pick' , img)

cv2.waitKey(0)

cv2.destroyAllWindows()
