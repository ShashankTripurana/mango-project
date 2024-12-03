import torch
from PIL import Image
import cv2

# Load YOLOv5 model (pre-trained on COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load your image
img = Image.open('H:/FRUIT PHOTOS-20240721T154238Z-001/FRUIT PHOTOS/F2 B F.JPG')

# Perform inference
results = model(img)

# Show the results
results.show()
