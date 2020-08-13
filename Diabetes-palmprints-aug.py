
import cv2
import numpy as np
from skimage import io 
from skimage.transform import rotate, AffineTransform, warp
import matplotlib.pyplot as plt
import random
from skimage import img_as_ubyte
import os
from skimage.util import random_noise


def v_flip(image): 
    return np.flipud(image) 

def h_flip(image): 
    return np.fliplr(image) 

#uses sklearn rotate method 
def clockwise_rotation(image):
    angle = random.randint(0,180)
    return rotate(image, -angle) 

def anticlockwise_rotation(image): 
    angle = random.randint(0,180) 
    return rotate(image, angle) 

#uses skimage library to add random noise, random_noise() method
def add_noise(image): 
    return random_noise(image)

#blurring with gaussian_blur() from openCV 
def blur_img(image): 
    return cv2.GaussianBlur(image, (7,7), 0)

#use a dict to store function names
augmentation = { 'vertical flip':v_flip, 
                'horizontal flip':h_flip, 
                'rotate clockwise':clockwise_rotation, 
                'rotate anti-clockwise':anticlockwise_rotation,
                'blurring':blur_img,
                'adding noise':add_noise  
               } 

images = [] 

#src_path - the path to original dataset 
#augmented_path - where you want to save augmented images 
#replace both as per your machine 

def augment(src_path, augmented_path):
    for img in os.listdir(src_path): 
        images.append(os.path.join(src_path, img)) 

    #no. of images you want to generate 
    if src_path == '/home/cas/Desktop/Proiect/barbatisanatosi/dreapta/':
        imgs_to_generate = 2500 
    else: 
        imgs_to_generate = 500
    i = 1

    while i <= imgs_to_generate: 
        img = random.choice(images)
        original_img = io.imread(img) 
        transformed_img = None 

        n = 0 
        transform_count = random.randint(1, len(augmentation)) 

        while n <= transform_count: 
            key = random.choice(list(augmentation)) #method to call on img 
            transformed_img = augmentation[key](original_img)
            n += 1

        new_img_path = "%s/augmented_image_%s.jpg" %(augmented_path, i)
        transformed_img = img_as_ubyte(transformed_img)
        transformed_img = cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB) 
        cv2.imwrite(new_img_path, transformed_img) 
        i += 1 

#eg.
#augment('/home/cas/Desktop/Proiect/dz1barbati/dreapta/', '/home/cas/Desktop/Proiect/dz1barbati_aug/')

