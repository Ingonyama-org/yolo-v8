import random
import os
import shutil


def make_dir(val, test, train):
    data = [val, test, train]
    data_fldr = ['images', 'labels']

    for d in data:
        for df in data_fldr:
            os.makedirs(os.path.join(d, df))


def move_files(IMG_DIR, DATA_DIR, data, class_list):
    try:
        img = random.choice([image for image in os.listdir(IMG_DIR)])
        img_path = os.path.join(IMG_DIR, img)
        label_path = os.path.join(os.path.join(DATA_DIR,'labels'), img.replace("jpg", 'txt'))
        shutil.move(img_path, os.path.join(data, 'images'))
        shutil.move(label_path, os.path.join(data, 'labels'))

        if not os.path.exists(os.path.join(data, 'labels',"class.txt")):
            with open(os.path.join(data, 'labels', 'class.txt'), 'w') as f:
                for count, label in enumerate(class_list):
                    f.write(f'{label}\n') if count != len(class_list)-1 else f.write(f'{label}')
    except:
        with open(os.path.join(os.path.join(DATA_DIR,'labels'), img.replace("jpg", 'txt')), 'w') as lf:
            lf.write(f'{class_list.index("nothing")} 0 0 0 0')
        shutil.move(os.path.join(os.path.join(DATA_DIR,'labels'), img.replace("jpg", 'txt')), os.path.join(data, 'labels'))
            
def if_float(dl, no):
        train_data_len = 0
        if isinstance(dl * no, float):
            train_data_len = int(dl * no) + 1
        else:
            train_data_len = dl * no
        return train_data_len

def split_data(data_len, IMG_DIR, DATA_DIR, TRAIN_DATA, VAL_DATA, TEST_DATA, class_list):
    print(f'\n{"="*20} SPLITING DATA {"="*20}\n')

    if os.path.exists(TRAIN_DATA):
        shutil.rmtree(TRAIN_DATA)
        shutil.rmtree(VAL_DATA)
        shutil.rmtree(TEST_DATA)
            
    make_dir(VAL_DATA, TEST_DATA, TRAIN_DATA )

    for count in range(data_len):
        if count <= if_float(data_len, .7):
            move_files(IMG_DIR, DATA_DIR, TRAIN_DATA, class_list)
        elif count > int(data_len*.7) and count <= int(data_len * .9):
            move_files(IMG_DIR, DATA_DIR, VAL_DATA, class_list)
        elif count > int(data_len * .9):
            move_files(IMG_DIR, DATA_DIR, TEST_DATA, class_list)

    shutil.rmtree(os.path.join(DATA_DIR, 'images'))
    shutil.rmtree(os.path.join(DATA_DIR, 'labels'))

    print(f'\n{"="*20} DONE SPLITING {"="*20}\n')
