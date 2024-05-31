import os


def change_class_ids_in_labels(label_dir, class_id_mapping):
    # Iterate over all label files in the directory
    for filename in os.listdir(label_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(label_dir, filename)
            with open(filepath, 'r') as f:
                lines = f.readlines()
            with open(filepath, 'w') as f:
                # Replace old_class_id with new_class_id in each line
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) > 0:
                        old_class_id = int(parts[0])
                        if old_class_id in class_id_mapping:
                            parts[0] = str(class_id_mapping[old_class_id])
                    f.write(' '.join(parts) + '\n')


# Example usage:
label_dir = 'datasets/anno_poly/yolo_labels_updated'
class_id_mapping = {0: 29, 1: 30, 2: 31}  # Example mapping from old class IDs to new class IDs

# Change class IDs in the label directory
change_class_ids_in_labels(label_dir, class_id_mapping)
