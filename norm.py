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
            filepath = pseudoroot + '/' + folder + '/' + file

            imtemp = ski.io.imread(filepath, as_gray = False, plugin = None)
            imtemp = imtemp.astype(float)

            img += imtemp

            #print(filepath)
            i = i + 1

        img /= i
        #salvar imagem média#####################

        img = img/255
        img[:, :, 0] = img[:, :, 0]*0.2125
        img[:, :, 1] = img[:, :, 1]*0.7154
        img[:, :, 2] = img[:, :, 2]*0.0721

        img2 = img[:,:,0] + img[:,:,1] + img[:,:,2]   

        img2 = ski.util.img_as_ubyte(img2)

        img2 = np.reshape(img2, -1)
        plt.hist(img2, bins = 255)

        mean = np.mean(img2)
        var = np.var(img2)
        print(img2.shape, img2, var)

        #plt.imshow(img2, cmap = 'gray')
        plt.show()
    



if __name__ == "__main__":
    main()
