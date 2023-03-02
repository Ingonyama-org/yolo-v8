import os
import tqdm
import json


def convert_jsonLabels_to_yoloFormat(IMG_DIR, DATA_DIR, class_list):
    print(f'\n{"="*20} CONVERTING JSON TO YOLO FORMAT {"="*20}\n')
    count = 0
    for image in os.listdir(IMG_DIR):
        label_path = os.path.join(DATA_DIR, 'labels', image.replace('jpg', 'json'))

        try:
            with open(label_path, 'r') as f:
                json_f = json.loads(f.read())
                for shape_index in range(len(json_f['shapes'])):
                    label = class_list.index(json_f['shapes'][shape_index]['label'])
                    x_min = json_f['shapes'][shape_index]['points'][0][0]
                    y_min = json_f['shapes'][shape_index]['points'][0][1]
                    x_max = json_f['shapes'][shape_index]['points'][1][0]
                    y_max = json_f['shapes'][shape_index]['points'][1][1]
                
                    x_center = ((x_min + x_max )/2)/json_f['imageWidth']
                    y_center = ((y_min + y_max )/2)/json_f['imageHeight']
                    width = (max(x_max, x_min) - min(x_max, x_min))/json_f['imageWidth']
                    height = (max(y_max, y_min) - min(y_max, y_min))/json_f['imageHeight']

                    with open(os.path.join(DATA_DIR, 'labels', image.replace('jpg', 'txt')), 'a') as f:
                        f.write(f'{label} {x_center} {y_center} {width} {height}\n') if shape_index != len(json_f['shapes'])-1 else f.write(f'{label} {x_center} {y_center} {width} {height}')
            os.remove(label_path)
        except:
            with open(os.path.join(DATA_DIR, 'labels', image.replace('jpg', 'txt')), 'w') as empty_f:
                empty_f.write(f'{class_list.index("nothing")} 0 0 0 0')
        
       
    print(f'\n{"="*20} DONE CONVERTING {"="*20}\n')











































# def convert_jsonLabels_to_yoloFormat(IMG_DIR, class_list, IMG_SIZE, loop=0):
#     
#     while loop < 2:
#         for image in os.listdir(os.path.join(IMG_DIR)):
#             label_path = os.path.join('d_data','labels', f'{image.split(".")[0]}.json')
#             if not os.path.exists(os.path.join('d_data','labels', f'{image.split(".")[0]}.txt')):
#                 if os.path.exists(label_path):
#                     with open(label_path, 'r') as f:
#                         label = json.load(f)
#                     new_label_path = label_path.replace('.json', '.txt')            
                    
#                     for shape in range(len(label['shapes'])):
#                         box_width = (label['shapes'][shape]['points'][1][0]-label['shapes'][shape]['points'][0][0])
#                         box_height = (label['shapes'][shape]['points'][1][1]-label['shapes'][shape]['points'][0][1])

#                         object_class= class_list.index(label['shapes'][shape]['label'])
#                         x_center = ((label['shapes'][shape]['points'][0][0]+label['shapes'][shape]['points'][1][0])/2)/IMG_SIZE
#                         y_center = ((label['shapes'][shape]['points'][0][1]+label['shapes'][shape]['points'][1][1])/2)/IMG_SIZE
#                         width = box_width/IMG_SIZE
#                         height = box_height/IMG_SIZE
                        
#                         with open(new_label_path, 'a') as fp:
#                             fp.write(f'{object_class} {x_center} {y_center} {width} {height}\n')
#                     os.remove(label_path)
#                 else:
#                     empty_label_path = os.path.join('d_data','labels', f'{image.split(".")[0]}.txt')
#                     with open(empty_label_path, 'w') as fp:
#                         fp.write(f'0 0 0 0 0')

#         with open(os.path.join('d_data','labels', "classes.txt"), 'w') as fp:
#             for object_class_name in class_list:
#                 fp.write(f"{object_class_name}\n")
#         loop += 1

#     print(f'\n{"="*20} DONE CONVERTING {"="*20}\n')