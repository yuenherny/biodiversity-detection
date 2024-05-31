import json
import os
from shapely.geometry import Polygon
from PIL import Image


def polygon_to_yolo_bbox(polygon, image_width, image_height):
    # Convert the polygon points to a shapely Polygon
    poly = Polygon(polygon)

    # Get the bounding box of the polygon
    minx, miny, maxx, maxy = poly.bounds

    # Convert to YOLO format (normalized center x, center y, width, height)
    x_center = (minx + maxx) / 2.0 / image_width
    y_center = (miny + maxy) / 2.0 / image_height
    width = (maxx - minx) / image_width
    height = (maxy - miny) / image_height

    return x_center, y_center, width, height


def convert_json_to_yolo(json_file, output_txt_file, image_width, image_height, class_names):
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(output_txt_file, 'w') as f:
        for item in data['shapes']:
            class_name = item['label']
            if class_name in class_names:
                class_id = class_names.index(class_name)
                polygon = item['points']

                # Convert polygon to YOLO bounding box format
                x_center, y_center, width, height = polygon_to_yolo_bbox(polygon, image_width, image_height)

                # Write the YOLO formatted bounding box to the output file
                f.write(f'{class_id} {x_center} {y_center} {width} {height}\n')


def convert_dataset(json_labels_dir, yolo_labels_dir, images_dir, class_names):
    os.makedirs(yolo_labels_dir, exist_ok=True)
    for json_file in os.listdir(json_labels_dir):
        if json_file.endswith('.json'):
            image_file = os.path.join(images_dir, os.path.splitext(json_file)[0] + '.png')
            if os.path.exists(image_file):
                # Get the dimensions of the image
                with Image.open(image_file) as img:
                    image_width, image_height = img.size
                output_txt_file = os.path.join(yolo_labels_dir, os.path.splitext(json_file)[0] + '.txt')
                convert_json_to_yolo(os.path.join(json_labels_dir, json_file), output_txt_file, image_width, image_height, class_names)


# Define class names and paths
class_names = ['biodiversity_A', 'biodiversity_B']
json_labels_dir = 'datasets/anno_poly/coco_labels'
yolo_labels_dir = 'datasets/anno_poly/yolo_labels'
images_dir = 'datasets/Images/Biodiversity'

# Convert the entire dataset
convert_dataset(json_labels_dir, yolo_labels_dir, images_dir, class_names)
