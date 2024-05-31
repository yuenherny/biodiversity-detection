import os
import xml.etree.ElementTree as ET


def convert_voc_to_yolo(xml_file, output_txt_file, class_names):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    with open(output_txt_file, 'w') as f:
        for obj in root.findall('object'):
            class_name = obj.find('name').text
            class_id = class_names.index(class_name)
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

            image_width = int(root.find('size/width').text)
            image_height = int(root.find('size/height').text)

            x_center = (xmin + xmax) / 2.0 / image_width
            y_center = (ymin + ymax) / 2.0 / image_height
            width = (xmax - xmin) / image_width
            height = (ymax - ymin) / image_height

            f.write(f'{class_id} {x_center} {y_center} {width} {height}\n')


def convert_dataset(voc_labels_dir, yolo_labels_dir, images_dir, class_names):
    print('Start converting dataset...')
    os.makedirs(yolo_labels_dir, exist_ok=True)
    for xml_file in os.listdir(voc_labels_dir):
        if xml_file.endswith('.xml'):
            image_file = os.path.join(images_dir, os.path.splitext(xml_file)[0] + '.png')
            if os.path.exists(image_file):
                # Assuming all images have the same dimensions. Alternatively, you can read each image to get its dimensions.
                output_txt_file = os.path.join(yolo_labels_dir, os.path.splitext(xml_file)[0] + '.txt')
                convert_voc_to_yolo(os.path.join(voc_labels_dir, xml_file), output_txt_file, class_names)
    print('Done converting dataset.')


# Define class names and paths
class_names = ['biodiversity_cable', 'biodiversity_seabed', 'biodiversity_fish']
voc_labels_dir = 'datasets/anno_bbox/voc_labels'
yolo_labels_dir = 'datasets/anno_bbox/yolo_labels'
images_dir = 'datasets/Images/Biodiversity'

# Convert the entire dataset
convert_dataset(voc_labels_dir, yolo_labels_dir, images_dir, class_names)
