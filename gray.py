import cv2
import matplotlib.pyplot as plt
import numpy as np

def process_image(image_path):
    # Load the image
    image = cv2.imread(r"H:\FRUIT PHOTOS-20240721T154238Z-001\FRUIT PHOTOS\F2 D F.JPG")

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform edge detection using Canny
    edges = cv2.Canny(gray_image, threshold1=75, threshold2=50)

    # Create a figure to display original and processed images side by side
    plt.figure(figsize=(10, 5))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Grayscale and Edge Detected Image
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Grayscale & Outline')
    plt.axis('off')

    plt.show()

# Example usage
process_image('path_to_your_image.jpg')
