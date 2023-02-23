import os
import uuid
from PIL import Image

def resize_images(base_dir, temp_dir, img_dir, width, height):
    os.makedirs(os.path.join(base_dir, temp_dir))
    if not os.path.exists(os.path.join(base_dir, temp_dir)):
        os.mkdir(os.path.join(base_dir, temp_dir))
    for img in os.listdir(os.path.join(img_dir)):
        try: 
            image_path = os.path.join(img_dir, img)
            image = Image.open(image_path)
            new_image = image.resize((width, height))
            new_image.save(os.path.join(base_dir, temp_dir, f'{str(uuid.uuid1())}.jpg'))
        except:
            pass
        os.remove(image_path)
    os.rmdir(os.path.join(img_dir))
    os.rename(os.path.join(base_dir, temp_dir), os.path.join(img_dir))