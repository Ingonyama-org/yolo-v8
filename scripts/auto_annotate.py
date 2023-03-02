import os
import ssl
import cv2
import tqdm
import torch
import json
import base64
import labelme

ssl._create_default_https_context = ssl._create_unverified_context


model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp9/weights/best.pt', force_reload=True)


def auto_annotation(DATA_DIR,IMG_DIR, IMG_SIZE):
    if not os.path.exists(os.path.join(os.path.join(DATA_DIR, 'labels'))):
        os.makedirs(os.path.join(DATA_DIR, 'labels'))

    print(f"\n---------ANNOTATING--------\n")
    for image in os.listdir(IMG_DIR):
        img_path = os.path.join(IMG_DIR, image)
        label_path = os.path.join(DATA_DIR, 'labels', image.replace('jpg', 'json'))
        
        img = cv2.imread(img_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        results = model(gray_img)

        all_labels=[]
        all_cods=[]
        repeat_count=0
        for name in range(len(results.pandas().xyxy[0].to_dict()["name"])):
            if results.pandas().xyxy[0].to_dict()["name"][name] in all_labels:
                if results.pandas().xyxy[0].to_dict()["confidence"][name] > results.pandas().xyxy[0].to_dict()["confidence"][all_labels.index(results.pandas().xyxy[0].to_dict()["name"][name])+repeat_count]:
                    try:
                        del all_labels[all_labels.index(results.pandas().xyxy[0].to_dict()["name"][name])+repeat_count] 
                    except:
                        pass
                else:
                    try:
                        del all_labels[name] 
                    except:
                        pass

                repeat_count +=1

            else: 
                all_labels.append(results.pandas().xyxy[0].to_dict()["name"][name])
                all_cods.append(results.pandas().xyxy[0].to_dict()["xmin"][name])
                all_cods.append(results.pandas().xyxy[0].to_dict()["ymin"][name])
                all_cods.append(results.pandas().xyxy[0].to_dict()["xmax"][name])
                all_cods.append(results.pandas().xyxy[0].to_dict()["ymax"][name])

        with open(label_path, 'w') as fp:
            shapes = []
            steps =0
            for index in range(len(all_labels)):
                shapes.append({
                    "label":all_labels[index], 
                    "points":[ all_cods[steps:steps+2], all_cods[steps+2:steps+4] ], 
                    "group_id": f'Null', 
                    "shape_type": "rectangle", 
                    "flags": {} })
                steps += 4
            fp.write(json.dumps({
                'version': f'{labelme.__version__}',
                'flags': {}, 
                'shapes': shapes, 
                "imagePath": f"..\\images\\{image}",
                "imageData":f"{base64.b64encode(labelme.LabelFile.load_image_file(img_path)).decode('utf-8')}",
                "imageHeight": IMG_SIZE,
                "imageWidth": IMG_SIZE
                })) 
    print(f"\n---------COMPLETED ANNOTATING--------\n")  
