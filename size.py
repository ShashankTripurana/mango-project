import cv2

def resize_image(image_path, output_path, width=None, height=None):
    # Load the image
    image = cv2.imread(image_path)

    # Get the original dimensions
    (h, w) = image.shape[:2]

    # If both the width and height are None, return the original image
    if width is None and height is None:
        resized = image
    elif width is None:
        # Calculate the ratio of the height and construct the new dimensions
        ratio = height / float(h)
        dim = (int(w * ratio), height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    elif height is None:
        # Calculate the ratio of the width and construct the new dimensions
        ratio = width / float(w)
        dim = (width, int(h * ratio))
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    else:
        # Resize to the specified width and height
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # Save the resized image
    cv2.imwrite(output_path, resized)

    return resized

# Example usage
input_image_path = r"H:\grap_3.png"
output_image_path = 'H:/resized_image3.jpg'

# Resize to specific width and height
resized_image = resize_image(input_image_path, output_image_path, width=300, height=200)

# Optionally, you can display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()