import numpy as np
import skimage as ski
import matplotlib.pyplot as plt

path = 'folhas_normalized/4_kale/'
im1path = path + '4-01-V1-W-Eq.png'
im2path = path + '4-01-V1-W.png'

img1 = ski.io.imread(im1path, as_gray= False, plugin= None)
img2 = ski.io.imread(im2path, as_gray= False, plugin= None)

img3 = np.abs(img1-img2)

print(np.max(img3))
plt.imshow(img3)
plt.show()
