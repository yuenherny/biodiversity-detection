from ultralytics import YOLO
from ultralytics.solutions import object_counter
import pandas as pd
import cv2
import os

# Load the trained model for prediction
model = YOLO('runs/detect/train40/weights/best.torchscript')
print(model.names)

# Predict on a videos
BASE_PATH = 'datasets/Videos'
# file_name = 'CHW01 FOU ROV monitoring_fish aggregation (08549122_A)'
file_name = 'CHW01 FOU ROV monitoring_C01 bottom to base -20230627 (08549120_A)'
source_media = os.path.join(BASE_PATH, f'{file_name}.mp4')

cap = cv2.VideoCapture(source_media)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

line_points = [(0, 400), (w, 400)]  # line or region points
classes_to_count = [0, 1, 2]  # all classes for count

# Video writer
video_writer = cv2.VideoWriter(
    f"ObjectCounter_{file_name}.avi",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (w, h)
)

counter = object_counter.ObjectCounter()
counter.set_args(view_img=True,
                 reg_pts=line_points,
                 classes_names=model.names,
                #  draw_tracks=True,
                 line_thickness=2,
                 region_thickness=1)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    tracks = model.track(im0, persist=True, show=False, classes=classes_to_count)

    im0 = counter.start_counting(im0, tracks)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()

df_count = pd.DataFrame(counter.class_wise_count)
df_count.to_csv(f'ObjectCounter_{file_name}.csv')
