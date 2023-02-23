import os
import json

def convert_jsonLabels_to_yoloFormat(IMG_DIR, class_list, IMG_WIDTH, IMG_HEIGHT):
    for image in os.listdir(os.path.join(IMG_DIR)):
        label_path = os.path.join('d_data','labels', f'{image.split(".")[0]}.json')
        if not os.path.exists(os.path.join('d_data','labels', f'{image.split(".")[0]}.txt')):
            if os.path.exists(label_path):
                with open(label_path, 'r') as f:
                    label = json.load(f)
                new_label_path = label_path.replace('.json', '.txt')            
                
                for shape in range(len(label['shapes'])):
                    box_width = (label['shapes'][shape]['points'][1][0]-label['shapes'][shape]['points'][0][0])
                    box_height = (label['shapes'][shape]['points'][1][1]-label['shapes'][shape]['points'][0][1])

                    object_class= class_list.index(label['shapes'][shape]['label'])
                    x_center = ((label['shapes'][shape]['points'][0][0]+label['shapes'][shape]['points'][1][0])/2)/IMG_WIDTH
                    y_center = ((label['shapes'][shape]['points'][0][1]+label['shapes'][shape]['points'][1][1])/2)/IMG_HEIGHT
                    width = box_width/IMG_WIDTH
                    height = box_height/IMG_HEIGHT
                    
                    with open(new_label_path, 'a') as fp:
                        fp.write(f'{object_class} {x_center} {y_center} {width} {height}\n')
                os.remove(label_path)
            else:
                empty_label_path = os.path.join('d_data','labels', f'{image.split(".")[0]}.txt')
                print(empty_label_path)
                with open(empty_label_path, 'w') as fp:
                    fp.write(f'0 0 0 0 0')

    with open(os.path.join('d_data','labels', "classes.txt"), 'w') as fp:
        for object_class_name in class_list:
            fp.write(f"{object_class_name}\n")