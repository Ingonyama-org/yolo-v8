import os
import yaml

def train(CLASS_LIST,DATA_DIR, YAML_PATH, pre_trained_model,IMG_SIZE, epochs):  
    labels={}
    for index, item in enumerate(CLASS_LIST):
        labels[index] = item

    YAML_DATA = {
        'val': 'val/images',
        'test': 'test/images',
        'train':'train/images',
        'path': f'../{DATA_DIR}',
        "names": labels,
        'nc': len(CLASS_LIST)
    }

    with open(YAML_PATH, 'w') as yaml_file:
        yaml_file.write( yaml.dump(YAML_DATA, default_flow_style=False))
   
    os.system(f'yolo task=detect mode=train model={pre_trained_model} data={YAML_PATH} imgsz={IMG_SIZE} epochs={epochs}' )
    
    
 