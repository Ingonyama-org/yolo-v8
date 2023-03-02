import os
import cv2
import numpy as np

def predict_on_image(model ,UNDETECTED_LIONS, DETECTED_IMAGES, CLASS_LIST, conf):
    for image in os.listdir(UNDETECTED_LIONS):
        image_path = os.path.join(f'{UNDETECTED_LIONS}',image)
        result = model(image_path, conf=conf)[0]

        # detection
        cls = result.boxes.cls.cpu().numpy()  
        probs = result.boxes.conf.cpu().numpy() 
        boxes = result.boxes.xyxy.cpu().numpy()   

        if not os.path.exists(DETECTED_IMAGES):
            os.makedirs(DETECTED_IMAGES)
        
        os.makedirs(os.path.join(DETECTED_IMAGES, image.split(".")[0]))

        img = cv2.imread(image_path)

        for box_index in range(len(boxes)):
            
            x_min = int(boxes[box_index].tolist()[0])
            y_min = int(boxes[box_index].tolist()[1])
            x_max = int(boxes[box_index].tolist()[2])
            y_max = int(boxes[box_index].tolist()[3])

            cropped_image = img[y_min:y_max, x_min:x_max]

            imgname = f'{CLASS_LIST[cls[box_index].astype(int)] }_{(probs[box_index])*100:.2f}%.jpg'
            cv2.imwrite(os.path.join(DETECTED_IMAGES, image.split(".")[0], imgname), cropped_image)