from rembg import remove as rem
import matplotlib.pyplot as plt
import skimage as ski
import numpy as np
import os

def main():

    source_root = 'folhas_mask'

    for folder in sorted(os.listdir(source_root)):
        print (folder)
    
        for file in sorted(os.listdir(source_root + '/' + folder)):
            if file[-5] == 'B' and file[-7] == '1':
                continue
            
            source_path = source_root + '/' + folder + '/' + file

            img = ski.io.imread(source_path)

            bgrem = rem(img)
            output_gray = 255*(1 - ski.color.rgb2gray(ski.color.rgba2rgb(bgrem))) 
            output_gray.astype(np.uint8)

            output_bin = output_gray > 5

            ski.io.imsave(source_path, ski.img_as_uint(output_bin))
            
        break

if __name__ == "__main__":
    main()