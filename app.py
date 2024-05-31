import os
import streamlit as st
from ultralytics import YOLO
from collections import Counter
import pandas as pd
import cv2
from PIL import Image
import numpy as np


# Function to draw bounding boxes using YOLO results
def draw_bounding_boxes(image, results, color_map):
    # Load image using PIL
    img = Image.open(image).convert("RGB")

    # Convert PIL image to OpenCV format (numpy array)
    img = np.array(img)

    # Draw bounding boxes
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f'{result.names[cls]} {conf:.2f}'
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color_map[cls], 2)
            cv2.putText(img, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color_map[cls], 2)

    # Convert back to PIL image
    img = Image.fromarray(img)
    return img


def prediction_to_dataframe(results):
    class_names = results[0].names
    class_ids = []
    for result in results:
        for box in result.boxes:
            class_ids.append(int(box.cls))

    class_id_count = Counter(class_ids)
    class_count = {class_names[key]: class_id_count[key] for key in class_id_count}

    return pd.DataFrame(class_count, index=range(1))


# Navigation bar
st.markdown('KUL Coolies')

# Body
# col1, col2, col3 = st.columns(3)

# with col1:
    # st.image('bos_logo.png', width=100)

# with col3:
st.header('Bio Offshore Scanner')

uploaded_media = st.file_uploader("Choose media", key="1")

if uploaded_media is not None:
    # Save uploaded photo to a folder
    folder_path = "uploaded_files"
    os.makedirs(folder_path, exist_ok=True)

    uploaded_media_path = os.path.join(folder_path, uploaded_media.name)
    with open(uploaded_media_path, "wb") as f:
        f.write(uploaded_media.getbuffer())

    model = YOLO('runs/detect/train40/weights/best.torchscript')
    results = model.predict(uploaded_media_path, save=True, iou=0.1)

    class_mapping = {0: 'small_barnacle_cluster', 1: 'large_barnacle_cluster', 2: 'zero_biodiversity_on_cable'}
    color_mapping = {0: (255, 0, 0), 1: (0, 255, 0), 2: (0, 0, 255)}
    for result in results:
        for cls_id, custom_label in class_mapping.items():
            if cls_id in result.names:  # check if the class id is in the results
                result.names[cls_id] = custom_label  # replace the class name with the custom label
    
    image_with_boxes = draw_bounding_boxes(uploaded_media_path, results, color_map=color_mapping)

    # Display the image with bounding boxes
    st.dataframe(prediction_to_dataframe(results), use_container_width=True)
    st.image(image_with_boxes, use_column_width=True)
    
