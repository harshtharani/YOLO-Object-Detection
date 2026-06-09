from ultralytics import YOLO
import cv2

# Load the pretrained YOLO11 nano model
model = YOLO("yolo11n.pt")

# Perform object detection on the input image
results = model("test.jpg")

# Print detailed information about the detected bounding boxes
print(results[0].boxes)

# Draw bounding boxes, labels, and confidence scores on the image
annotated_image = results[0].plot()

# Display the annotated image in a window
cv2.imshow("YOLO Detection", annotated_image)

# Save the annotated image to the Output folder
cv2.imwrite(
    "Output/detected_image.jpg",
    annotated_image
)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()