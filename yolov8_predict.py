from ultralytics import YOLO
from ultralytics.solutions import object_counter
from collections import Counter
import pandas as pd
import cv2
import os

# Load the trained model for prediction
model = YOLO('runs/detect/train40/weights/best.torchscript')
print(model.names)

# Predict on a videos
BASE_PATH = 'datasets/Images'
file_name = 'Biodiversity'
source_media = os.path.join(BASE_PATH, file_name)

results = model.predict(source_media, save=True)

# class_names = results[0].names
# class_ids = []
# for result in results:
#     result.save_txt('results.txt', save_conf=True)
#     try:
#         class_ids.append(int(result.boxes.cls))
#     except Exception:
#         print('No detections in this frame.')

# class_id_count = Counter(class_ids)
# class_count = {class_names[key]: class_id_count[key] for key in class_id_count}

# df_count = pd.DataFrame(class_count, index=range(1))
