from PIL import Image
from pprint import pprint


import argparse
import cv2 as cv
import numpy as np
import os
import time


# Set image dataset here
IMG_DATASET = 'konbini'
SUPPORTED_IMAGE_TYPES = {'jpg', 'jpeg', 'png',}
IMG_FOLDER = 'pictures'

parser = argparse.ArgumentParser(description='Image Blender, --st to show transition')
parser.add_argument('-show-transition', '--st', type=bool, default=False, help='Whether to show transition')
args = parser.parse_args()


def blend(ifile1, ifile2, cur_step, step):
    #print(ifile1, ifile2, cur_step, step)
    img1, img2  = cv.imread(ifile1), cv.imread(ifile2)
    #img1, img2 = cv.cvtColor(img1, cv.COLOR_BGR2RGB), cv.cvtColor(img2, cv.COLOR_BGR2RGB) 
    start, end = 0, 1

    for idx, i in enumerate(np.linspace(start, end, step)):
        #if idx + 1 == len(np.linspace(start, end, step)):
        #    continue
        print(cur_step, idx, step)
        alpha = i
        beta = 1 - alpha
        if idx != 0:
            output = cv.addWeighted(img2,alpha,img1,beta,0)
        else:
            output = img1
        #output = np.clip(output * 255, 0, 255) # proper [0..255] range
        #output = output.astype(np.uint8)  # safe conversion

        #print(args.st, type(args.st))
        #output = cv.cvtColor(output, cv.COLOR_BGR2RGB)
        if args.st:
            cv.imshow('Transition Effect ', output)
            time.sleep(.25)
            if cv.waitKey(1) == 27:
                break
        #print(output, type(output))
        #print(idx+cur_step, alpha, beta)

        cv.imwrite(f"{IMG_FOLDER}/{IMG_DATASET}/generated/{idx+cur_step}-{IMG_DATASET}.jpeg", output)
        #im_output = Image.fromarray(output)
        #im_output.save(f"{IMG_FOLDER}/{IMG_DATASET}/generated/{idx+cur_step+1}-{IMG_DATASET}.jpeg")
        #print(f"Saving image {IMG_FOLDER}/{IMG_DATASET}/generated/{idx}-{IMG_DATASET}.jpeg")
                
def load_files():
    files = os.listdir(f'{IMG_FOLDER}/{IMG_DATASET}/source')
    img_files = []

    for f in files:
        for img_type in SUPPORTED_IMAGE_TYPES:
            if f.endswith(img_type):
                img_files.append(f'{IMG_FOLDER}/{IMG_DATASET}/source/' + f)
                break
  
    img_files = sorted(img_files)
    return img_files

if __name__ == '__main__':
    files = load_files()
    flen = len(files)
    print("Using images as source:")
    pprint(files)

    step = 24 / flen
    if int(step) != step:
        raise ValueError("The number of files must be a number that can divide into 24 without resulting in a rational number.")
    step = int(step)

    for i in range(flen):
        #print(i, (i+1)%flen)
        blend(files[i], files[(i+1)%flen], int(i*step), step)
