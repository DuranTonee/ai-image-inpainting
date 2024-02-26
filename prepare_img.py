import cv2
import numpy as np

def transform_image(square_size):
    # Load original image
    original_img = cv2.imread('original_image.jpg')

    # Find the minimum dimension to determine the size of the square
    min_dim = min(original_img.shape[0], original_img.shape[1])

    # Crop a square from the center
    start_x = (original_img.shape[1] - min_dim) // 2
    start_y = (original_img.shape[0] - min_dim) // 2
    cropped_img = original_img[start_y:start_y+min_dim, start_x:start_x+min_dim]

    # Resize the cropped square to 500x500
    resized_img = cv2.resize(cropped_img, (square_size, square_size))

    # Create a transparent background
    background = np.zeros((1024, 1024, 4), dtype=np.uint8)
    background[:, :] = (255, 255, 255, 0)  # Fill with fully transparent white color

    # Calculate the position to place the resized image onto the background
    x_offset = (background.shape[1] - square_size) // 2
    y_offset = (background.shape[0] - square_size) // 2

    # Place the resized image onto the background
    background[y_offset:y_offset+square_size, x_offset:x_offset+square_size, :3] = resized_img  # Copy RGB channels
    background[y_offset:y_offset+square_size, x_offset:x_offset+square_size, 3] = 255  # Set alpha channel to fully opaque

    # Save the result
    cv2.imwrite('result_image.png', background)
    cv2.imwrite('cropped_image.jpg', resized_img)

if __name__ == "__main__":
    transform_image()