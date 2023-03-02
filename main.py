import os

from cv2 import displayOverlay
from scripts.detect import predict_on_image
from scripts.train import train
from scripts.resize import resize_images
from scripts.data_split import split_data 
from scripts.clean_dodgy import remove_dodgy_img
# from scripts.auto_annotate import auto_annotation
from scripts.convert_json_to_yolo import convert_jsonLabels_to_yoloFormat

from ultralytics import YOLO

DATA_DIR = 'd_data'

VAL_DATA = os.path.join(DATA_DIR, 'val')
TEST_DATA = os.path.join(DATA_DIR, 'test')
TRAIN_DATA = os.path.join(DATA_DIR, 'train')

IMG_DIR = os.path.join(DATA_DIR,'images')
YAML_PATH = os.path.join('scripts','dateset.yaml')

IMG_SIZE=512

IMAGE_EXTS = ['jpg', 'png']

CLASS_LIST = [
        "body",
        "nose",
        'nothing',
        "profile",
        "left_ear",
        "left_eye",
        "right_eye",
        "right_ear",
        "leftside_whiskers",
        "rightside_whiskers",
    ]

DETECTED_IMAGES = 'detected_lions'

UNDETECTED_LIONS = os.path.join('d_data', 'test', 'images')

#1. REMOVE THE DODGY IMAGES
# remove_dodgy_img(IMG_DIR, IMAGE_EXTS) 

#2. RESIZE ALL IMAGES
# resize_images(DATA_DIR,"clean_images", IMG_DIR, IMG_SIZE, IMG_SIZE)

#3. AUTO ANNOTATION
# auto_annotation(DATA_DIR,IMG_DIR, IMG_SIZE, IMG_SIZE)

#4. CONVERT JSON LABELS TO YOLO FORMAT
# convert_jsonLabels_to_yoloFormat(IMG_DIR,DATA_DIR, CLASS_LIST)

#5. SPLIT DATA
# split_data(len(os.listdir(IMG_DIR)), IMG_DIR, DATA_DIR, TRAIN_DATA, VAL_DATA, TEST_DATA, CLASS_LIST)

#6. TRAIN
# train(CLASS_LIST, DATA_DIR, YAML_PATH, '../yolov8n.pt', IMG_SIZE, epochs=100)

#7. DETECT
# predict_on_image(YOLO("runs/detect/train/weights/best.pt"),UNDETECTED_LIONS, DETECTED_IMAGES, CLASS_LIST, conf=0.6)




   
