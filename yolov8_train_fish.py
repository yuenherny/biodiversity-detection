import os
import random
import shutil
from ultralytics import YOLO

# Create a temporary yaml config
dataset_yaml = 'temp_dataset.yaml'
with open(dataset_yaml, 'w') as f:
    f.write("""
    train: TestFish/train/images
    val: TestFish/val/images
    
    nc: 32  # number of classes
    names: ['Acanthuridae -Surgeonfishes-', 'Balistidae -Triggerfishes-', 'Carangidae -Jacks-', 'Ephippidae -Spadefishes-', 'Labridae -Wrasse-', 'Lutjanidae -Snappers-', 'Pomacanthidae -Angelfishes-', 'Pomacentridae -Damselfishes-', 'Scaridae -Parrotfishes-', 'Scombridae -Tunas-', 'Serranidae -Groupers-', 'Shark -Selachimorpha-', 'Zanclidae (Moorish Idol)', 'Zanclidae -Moorish Idol-', 'angel', 'damsel', 'grouper', 'jack', 'parrot', 'shark', 'snapper', 'spade', 'surgeon', 'trigger', 'tuna', 'wrasse','Indo-Pacific sergeant','blue sea chub','Brassy Drummer', 'small_barnacle_cluster', 'large_barnacle_cluster', 'zero_biodiversity_on_cable']  # class names
    """)

# Load the YOLOv8 model
# model = YOLO('yolov8m.yaml').load('yolov8m.pt')
model = YOLO('yolov8n')

# Train the model
results = model.train(
    data=dataset_yaml,
    # hyperparameters
    imgsz=640,
    # freeze=13,
    # dropout=0.01,
    epochs=1,
    # augmentation
    # degrees=180,
    # translate=0.2,
    # shear=180,
    # perspective=0.01,
)
print(model.names)

# Save the trained model
model.export()

# Clear temporary directories
# clear_temp_directories()
