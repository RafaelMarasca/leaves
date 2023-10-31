import numpy as np
import skimage as ski
import scipy.signal as sps
import os

import matplotlib.pyplot as plt

def main():
    source_root = 'folhas_augmented'
    target_root = 'folhas_normalized'

    for folder in sorted(os.listdir(source_root)):
        print (folder)

        #Navigates through image files
        for file in sorted(os.listdir(source_root + '/' + folder)):
            if file[-5] != 'B' and file[-5] != 'W' and file[-5] != 'E' and file[-5] != 'L' and file[-5] != 'M':
                continue
            
            #Gets the image's relative path
            source_path = source_root + '/' + folder + '/' + file
            target_path = target_root + '/' + folder + '/' + file

            #Opens the image
            source_image = ski.io.imread(source_path, as_gray = False, plugin = None)

            #Converts image from RGB to HSV and extracts its V channel
            hsv_image = ski.color.rgb2hsv(source_image)
            v = hsv_image[:, :, 2]
            v = ski.util.img_as_ubyte(v)

            #Gets histogram from V channel, normalizes it, gets its CDF transform (adjusting it to integer max val = 255)
            #and equalizes the image's v channel in the s variable.
            hist, bins = np.histogram(v, bins = 256)
            hist = hist/(512*512)
            s = 255*np.cumsum(hist)
            s = np.round(s)
            img_eq = s[v]

            #Converts image back from HSV to RGB 
            img_eq = np.stack([hsv_image[:, :, 0], hsv_image[:, :, 1], img_eq/255], 2)
            img_eq = ski.color.hsv2rgb(img_eq)
            img_eq = ski.util.img_as_ubyte(img_eq)

            #Removes the extension and saves image to new path
            newpath = target_path[:-4]
            ski.io.imsave(newpath + '-Eq.png', img_eq)

            #plt.imshow(img_eq)
            #plt.show()


if __name__ == "__main__":
    main()
