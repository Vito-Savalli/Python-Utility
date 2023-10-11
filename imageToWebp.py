import os
import cv2

# Specify the folder path for your Desktop
folder_path = os.path.expanduser("~/Desktop")

# Iterate over the images on the Desktop
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust the file extensions as needed

        # Load the image
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)

        # Check if the image was loaded correctly
        if image is None:
            print(f"Error loading {filename}. Skipping...")
            continue

        # Save the image in webp format directly on the Desktop
        output_filename = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(folder_path, output_filename)
        cv2.imwrite(output_path, image)

        # Delete the original image
        os.remove(image_path)

print("Conversion finished!")
