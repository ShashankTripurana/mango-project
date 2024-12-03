import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
image = cv2.imread("H:/gray_unripe.png", cv2.IMREAD_GRAYSCALE)

# Display the original image
plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')


# Apply Gaussian Blur to remove noise
denoised_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the denoised image
plt.subplot(1, 3, 2)
plt.imshow(denoised_image, cmap='gray')
plt.title('Denoised Image')
plt.axis('off')


# Enhance the image using Histogram Equalization
enhanced_image = cv2.equalizeHist(denoised_image)

# Display the enhanced image
plt.subplot(1, 3, 3)
plt.imshow(enhanced_image, cmap='gray')
plt.title('Enhanced Image')
plt.axis('off')



# Show all images
plt.show()
