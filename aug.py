import numpy as np
import skimage as ski
import scipy.signal as sps
import os

import matplotlib.pyplot as plt


def image_log(img):
    img = img.astype(float)

    cl = 255 / np.log(1 + np.max(img))
    imglog = np.array(np.uint8(cl * np.log(1 + img)), dtype = np.uint8)

    return imglog


def image_gamma(img):
    img = img.astype(float)

    r = 2.4
    cr = 255 / np.power(255, r)
    imgrais = np.array(cr * np.power(img, r), dtype = np.uint8)

    return imgrais
  

def image_mean(img):
    img = img.astype(float)
    mean_kernel = np.array([[1/9, 1/9, 1/9],
                            [1/9, 1/9, 1/9],
                            [1/9, 1/9, 1/9]], dtype = float)
    
    imgmean = np.empty_like(img)

    for dim in range(img.shape[-1]):
        imgmean[:, :, dim] = sps.convolve2d(img[:, :, dim], mean_kernel, mode="same", boundary="symm")

    imgmean = imgmean.astype(np.uint8)
    

    return imgmean


def main():
    pseudoroot = 'folhas'
    for folder in sorted(os.listdir(pseudoroot)):
        print (folder)

        for file in sorted(os.listdir(pseudoroot + '/' + folder)):
            if file[-5] != 'B' and file[-5] != 'W':
                continue

            filepath = pseudoroot + '/' + folder + '/' + file

            im = ski.io.imread(filepath, as_gray = False, plugin = None)
    
            imlog = image_log(im)
            imrais = image_gamma(im)
            immean = image_mean(im)
            
            #fig, (ax1, ax2, ax3, ax4) = plt.subplots(ncols = 4, tight_layout = True)
            #ax1.imshow(im)
            #ax2.imshow(imlog)
            #ax3.imshow(imrais)
            #ax4.imshow(immean)
            #plt.show()

            newpath = filepath[:-4]

            ski.io.imsave(newpath + '-L.png', imlog)
            ski.io.imsave(newpath + '-E.png', imrais)
            ski.io.imsave(newpath + '-M.png', immean)


if __name__ == "__main__":
    main()
