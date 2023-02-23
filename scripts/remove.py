import os
import uuid

def remove_dodgy_img(IMG_DIR,image_exts ):
    for image in os.listdir(os.path.join(IMG_DIR)):
        if image == ".DS_Store":
            os.remove(os.path.join(IMG_DIR, image))
        else:
            image_path = os.path.join(IMG_DIR, image)
        if image_path.split('.')[-1] not in image_exts: 
            print(f'Image not in ext list {image_path}')
            os.remove(image_path)
        else:
            os.replace(image_path, os.path.join(IMG_DIR, f'{str(uuid.uuid1())}.jpg'))