import os
from scripts.resize import resize_images
from scripts.remove import remove_dodgy_img
# from scripts.auto_annotate import auto_annotation
from scripts.convert_json_to_yolo import convert_jsonLabels_to_yoloFormat


DATA_DIR = 'd_data'
IMG_DIR = os.path.join('d_data','images')

IMG_WIDTH=256
IMG_HEIGHT=256

IMAGE_EXTS = ['jpg', 'png']
CLASS_LIST = [
    'body', 
    'nose',  
    'nothing', 
    'profile',
    'left_ear', 
    'left_eye',
    'right_eye', 
    'right_ear', 
    'leftside_whiskers', 
    'rightside_whiskers',
     ]

#1. Remove the dodgy images
# remove_dodgy_img(IMG_DIR, IMAGE_EXTS)

#2. Resize all images to equal size
# resize_images(DATA_DIR,"clean_images", IMG_DIR, 500, 500)

#3. Auto annotation
# auto_annotation(DATA_DIR,IMG_DIR, IMG_WIDTH, IMG_HEIGHT)

#4. convert annotated json files to yolo format
# convert_jsonLabels_to_yoloFormat(IMG_DIR, CLASS_LIST, IMG_WIDTH, IMG_HEIGHT)

#5. Train
# cd yolov5 && sudo python3 train.py --img 72 --batch 16 --epochs 1000 --data dataset.yaml --weights yolov5s.pt --workers 2
