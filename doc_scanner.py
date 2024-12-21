import keras_ocr
import cv2  # For image reading and displaying
import matplotlib.pyplot as plt

# Initialize the OCR pipeline
pipeline = keras_ocr.pipeline.Pipeline()

# Load images
image_paths = ['test.jpg']  # List of image file paths
images = [cv2.imread(image_path) for image_path in image_paths]  # Read images as NumPy arrays

# Perform OCR
predictions = pipeline.recognize(images)


print(predictions)
# Process predictions, print recognized text, and draw annotations
# for image, prediction in zip(images, predictions):
#     # Extract recognized text
#     text = ' '.join([text for _, text in prediction])
    
#     # Print recognized text
#     print("Recognized text:", text)
    
#     # Draw annotations on the image
#     annotated_image = keras_ocr.tools.drawAnnotations(image=image, predictions=prediction)

#     # Display the annotated image
#     plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
#     plt.axis('off')  # Hide axis
#     plt.show()

#     # Optionally, save the annotated image
#     cv2.imwrite('annotated_image.jpg', annotated_image)
