import torchvision
import torch
import torchvision.transforms as transforms
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import glob
import shutil


def load_images(dir_files):
    """
    Moves the desired images into single folder, such that they can be used for the GAN
    :param dir_files:
    :return:
    """
    files = np.loadtxt(dir_files, dtype=str, delimiter=',')
    print(files)
    for file in files:
        source_path = './Data/imdb_crop/'+file
        dest_path = './Data/data/'+file[3:]
        try:
            shutil.move(source_path, dest_path)
        except FileNotFoundError:
            pass
    pass

num_images1 = len(np.loadtxt('./Data/only_women.csv', dtype=str, delimiter=',')) # num of images before moving
print(num_images1)
os.makedirs('./Data/data/') if not os.path.isdir('./Data/data/') else print('dir exists already')

image_gen = load_images('./Data/only_women.csv')

num_images2 = len(glob.glob('./Data/data/*')) # num of images after moving
print(num_images2)


