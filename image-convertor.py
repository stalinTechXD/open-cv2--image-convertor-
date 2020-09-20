import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('hell.png')

#change the color using the channels provided by the inbuilt python convertor
new_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)



plt.imshow(new_img)
plt.show()    