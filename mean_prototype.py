import numpy as np
import skimage as ski
import scipy.signal as sps
import os

import matplotlib.pyplot as plt

def main():
    source_root = 'folhas_augmented'
    target_root = 'folhas_mean_prototypes'
    
    for folder in sorted(os.listdir(source_root)):
        print (folder)

        #Variables to store the mean prototype initializes as empty arrays
        mean_img_w = np.zeros((512, 512, 3), dtype = float)
        mean_img_b = np.zeros((512, 512, 3), dtype = float)

        i_b = 0
        i_w = 0
        
        #Navigates through image files
        for file in sorted(os.listdir(source_root + '/' + folder)):
            if file[-5] != 'B' and file[-5] != 'W' and file[-5] != 'E' and file[-5] != 'L' and file[-5] != 'M':
                continue

            source_path = source_root + '/' + folder + '/' + file

            #Opens image and converts it to float
            source_image = ski.io.imread(source_path, as_gray = False, plugin = None)
            source_image = source_image.astype(float)

            #If it's a black image, adds to black mean variable, otherwise, adds it to white mean variable.
            if(file[-5] == 'B' or file[-7] == 'B'):
                mean_img_b += source_image
                i_b = i_b + 1

            elif(file[-5] == 'W' or file[-7] == 'W'):
                mean_img_w += source_image
                i_w = i_w + 1

        #Divides both black and white mean variables by the number of respective b&w images and saves them.
        mean_img_b /= i_b
        mean_img_w /= i_w

        mean_img_b_byte = mean_img_b.astype(np.uint8)
        mean_img_w_byte = mean_img_w.astype(np.uint8)

        ski.io.imsave(target_root + '/' + folder + '_' + 'mean_b_img.png', mean_img_b_byte)
        ski.io.imsave(target_root + '/' + folder + '_' + 'mean_w_img.png', mean_img_w_byte)

        '''
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
        '''


if __name__ == "__main__":
    main()
