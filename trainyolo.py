import os
import shutil
from sklearn.model_selection import train_test_split
import yaml



def split_data(images_dir, labels_dir, train_dir, val_dir, train_size=0.8):
    # Ensure output directories exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(os.path.join(train_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(train_dir, 'labels'), exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(os.path.join(val_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(val_dir, 'labels'), exist_ok=True)

    # List all image files
    image_files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

    # Split the dataset into training and validation sets
    train_files, val_files = train_test_split(image_files, train_size=train_size)

    # Function to copy files
    def copy_files(files, source_dir, target_dir):
        for f in files:
            # Copy image
            shutil.copy(os.path.join(source_dir, f), os.path.join(target_dir, 'images', f))
            # Copy corresponding label
            label_file = f.rsplit('.', 1)[0] + '.txt'
            shutil.copy(os.path.join(labels_dir, label_file), os.path.join(target_dir, 'labels', label_file))

    # Copy training files
    copy_files(train_files, images_dir, train_dir)
    # Copy validation files
    copy_files(val_files, images_dir, val_dir)

def create_dataset_yaml(train_dir, val_dir, class_names, yaml_file_path):
    dataset = {
        'train': train_dir,
        'val': val_dir,
        'nc': len(class_names),
        'names': class_names
    }

    # Write to a YAML file
    with open(yaml_file_path, 'w') as file:
        yaml.dump(dataset, file, sort_keys=False)




#split data
images_dir = 'images' 
labels_dir = 'labels'
train_dir = 'train'  
val_dir = 'val'        
split_data(images_dir, labels_dir, train_dir, val_dir)

#create yaml file
train_dir = '..\\train\\images'  
val_dir = '..\\val\\images'      
class_names = [str(i) for i in range(133)]  
yaml_file_path = 'dataset.yaml'
create_dataset_yaml(train_dir, val_dir, class_names, yaml_file_path)