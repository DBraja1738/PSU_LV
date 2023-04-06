import numpy as np
import matplotlib.pyplot as plt

def create_checkerboard(px_size,n_black,n_white):
    black_sq=np.zeros((px_size,px_size))
    white_sq=np.full((px_size,px_size),255)

    row_first=np.hstack([black_sq,white_sq]*int(n_white/2))
    row_sec=np.hstack([white_sq,black_sq]*int(n_white/2))

    checkerboard=np.vstack([row_first,row_sec]*int(n_black/2))
    return checkerboard
img=create_checkerboard(50,9,9)
plt.imshow(img,cmap="gray",vmin=0,vmax=255)
plt.show()