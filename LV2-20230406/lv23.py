import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("tiger.png")

#a)
img=img*2
plt.subplot(2,3,2)
plt.imshow(img,cmap="gray")

img = img[:,:,0].copy()
plt.subplot(2,3,1)
plt.imshow(img,cmap="gray")



#b)
(h,w)=img.shape
img_rot=np.zeros((w,h))
for i in range(0,h):
    img_rot[:,h-i-1]=img[i,:]
plt.subplot(2,3,3)
plt.imshow(img_rot,cmap="gray")
#c)
img_flip=np.zeros((h,w))
for i in range(0,h):
    img_flip[h-1-i,:]=img[i,:]
plt.subplot(2,3,4)
plt.imshow(img_flip,cmap="gray")
#d)
img_reduced=img[::10,::10]
plt.subplot(2,3,5)
plt.imshow(img_reduced,cmap="gray")

#e)
img_half=img
img_half[:,:w//4]=0
img_half[:,w//2:]=0
plt.subplot(2,3,6)
plt.imshow(img_half,cmap="gray")

plt.show()
