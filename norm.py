import numpy as np
import skimage as ski
import scipy.signal as sps
import os

import matplotlib.pyplot as plt

def main():
    pseudoroot = 'folhas_normalized'
    for folder in sorted(os.listdir(pseudoroot)):
        print (folder)

        img = np.zeros((512, 512, 3), dtype = float)

        i = 0;
        for file in sorted(os.listdir(pseudoroot + '/' + folder)):
            if file[-5] != 'B' and file[-5] != 'W' and file[-5] != 'E' and file[-5] != 'L' and file[-5] != 'M':
                continue

            filepath = pseudoroot + '/' + folder + '/' + file

            imtemp = ski.io.imread(filepath, as_gray = False, plugin = None)

            imgtemp4 = ski.color.rgb2hsv(imtemp)
            v = imgtemp4[:, :, 2]
            v = ski.util.img_as_ubyte(v)


            imtemp = imtemp.astype(float)

            img += imtemp

            imtemp2 = v

            hist, bins = np.histogram(imtemp2, bins = 256)

            hist = hist/(512*512)
            s = 255*np.cumsum(hist)
            s = np.round(s)

            img_eq = s[v]

            img_eq = np.stack([imgtemp4[:, :, 0], imgtemp4[:, :, 1], img_eq/255], 2)
            img_eq = ski.color.hsv2rgb(img_eq)
            img_eq = ski.util.img_as_ubyte(img_eq)

            newpath = filepath[:-4]
            ski.io.imsave(newpath + '-Eq.png', img_eq)

            plt.imshow(img_eq)
            plt.show()

            i = i + 1

        img /= i
        #salvar imagem média#####################
        imgmean = img.astype(np.uint8)
        ski.io.imsave(pseudoroot + '/' + folder + '/' + 'mean_img.png', imgmean)
        
        img = img/255
        img[:, :, 0] = img[:, :, 0]*0.2125
        img[:, :, 1] = img[:, :, 1]*0.7154
        img[:, :, 2] = img[:, :, 2]*0.0721

        img2 = img[:,:,0] + img[:,:,1] + img[:,:,2]   

        img2 = ski.util.img_as_ubyte(img2)

        img2 = np.reshape(img2, -1)
        #plt.hist(img2, bins = 256)
        
        var = np.var(img2)
        print(var)

        #plt.imshow(img2, cmap = 'gray')
        #plt.show()


if __name__ == "__main__":
    main()
