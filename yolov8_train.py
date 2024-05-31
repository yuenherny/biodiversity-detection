import os
import random
import shutil
from ultralytics import YOLO

# Define paths
image_dir = 'datasets/Images/Biodiversity'
label_dir = 'datasets/anno_poly/yolo_labels'
temp_train_images = 'datasets/temp/train/images'
temp_train_labels = 'datasets/temp/train/labels'
temp_val_images = 'datasets/temp/val/images'
temp_val_labels = 'datasets/temp/val/labels'

# Create temporary directories
os.makedirs(temp_train_images, exist_ok=True)
os.makedirs(temp_train_labels, exist_ok=True)
os.makedirs(temp_val_images, exist_ok=True)
os.makedirs(temp_val_labels, exist_ok=True)


def aggregate_images_and_labels(source_dirs, aggregated_image_dir, aggregated_label_dir):
    os.makedirs(aggregated_image_dir, exist_ok=True)
    os.makedirs(aggregated_label_dir, exist_ok=True)

    for source_dir in source_dirs:
        for file_name in os.listdir(source_dir['images']):
            if file_name.endswith('.jpg') or file_name.endswith('.png'):
                shutil.copy(os.path.join(source_dir['images'], file_name), aggregated_image_dir)
                label_file = os.path.join(source_dir['labels'], os.path.splitext(file_name)[0] + '.txt')
                if os.path.exists(label_file):
                    shutil.copy(label_file, aggregated_label_dir)


# Function to split dataset randomly
def split_dataset(image_dir, label_dir, train_ratio=0.8):
    images = [f for f in os.listdir(image_dir) if f.endswith('.png') or f.endswith('.png')]
    random.shuffle(images)
    split_idx = int(len(images) * train_ratio)
    train_images = images[:split_idx]
    val_images = images[split_idx:]

    for img in train_images:
        base_name = os.path.splitext(img)[0]
        if os.path.exists(os.path.join(label_dir, base_name + '.txt')):
            shutil.copy(os.path.join(image_dir, img), temp_train_images)
            shutil.copy(os.path.join(label_dir, base_name + '.txt'), temp_train_labels)
    
    for img in val_images:
        base_name = os.path.splitext(img)[0]
        if os.path.exists(os.path.join(label_dir, base_name + '.txt')):
            shutil.copy(os.path.join(image_dir, img), temp_val_images)
            shutil.copy(os.path.join(label_dir, base_name + '.txt'), temp_val_labels)


# Function to clear temporary directories
def clear_temp_directories():
    shutil.rmtree(temp_train_images)
    shutil.rmtree(temp_train_labels)
    shutil.rmtree(temp_val_images)
    shutil.rmtree(temp_val_labels)


# Split the dataset
# split_dataset(image_dir, label_dir, train_ratio=0.8)

# Create a temporary yaml config
dataset_yaml = 'temp_dataset.yaml'
with open(dataset_yaml, 'w') as f:
    f.write("""
    train: temp/train/images
    val: temp/val/images
    
    nc: 3  # number of classes
    names: ['biodiversity_A', 'biodiversity_B', 'biodiversity_C']  # class names
    """)

# Load the YOLOv8 model
# model = YOLO('yolov8m.yaml').load('yolov8m.pt')
model = YOLO('yolov8m')

# Train the model
results = model.train(
    data=dataset_yaml,
    # hyperparameters
    imgsz=640,
    freeze=13,
    dropout=0.01,
    epochs=10,
    # augmentation
    degrees=180,
    translate=0.2,
    shears=180,
    perspective=0.01,
)
print(model.names)

# Save the trained model
model.export()

# Clear temporary directories
# clear_temp_directories()
