# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 12:08:00 2018

@author: Grbic
"""

import scipy as sp
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#try:
#    face = sp.face(gray=True)
#except AttributeError:
#    from scipy import misc
#    face = misc.face(gray=True)
    
s1= mpimg.imread("example_grayscale.png",) # We need an (n_sample, n_feature) array
x=s1.reshape((-1,1))
k_means = cluster.KMeans(n_clusters=3,n_init=1)
k_means.fit(x) 
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = s1.shape

plt.figure(1)
plt.imshow(s1,  cmap='gray')
plt.show()

plt.figure(2)
plt.imshow(face_compressed,  cmap='gray')
plt.show()