import os
import glob
from scipy import misc
import numpy as np

def flip_and_save_images(img_dir, extension):
    os.chdir(img_dir)
    files = glob.glob("*." + extension)
    
    total_num = 0
    for i, file in enumerate(files):
        img = misc.imread(file, flatten=False, mode='RGB')
        flipped_img = np.fliplr(img)
        misc.imsave("flipped" + file, flipped_img)
        total_num += 1
       
    print(total_num, ' files have been flipped.')

# train_mask_dir = "../data/train/masks/"
# flip_and_save_images(train_mask_dir, "png")

train_images_dir = "../data/train/images/"
flip_and_save_images(train_images_dir, "jpeg")