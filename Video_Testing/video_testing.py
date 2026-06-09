from ultralytics import YOLO
import cv2

# Load the pretrained YOLO11 nano model
model = YOLO("yolo11n.pt")

# Specify the path to the input video
video_path = "samples_data_vtest.avi"

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get the video's frames per second (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the width and height of the video frames
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec to be used for the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create a VideoWriter object to save the output video
out = cv2.VideoWriter(
    "Output/yolo_detected_video.avi",
    fourcc,
    fps,
    (width, height)
)

# Process the video frame by frame
while True:

    # Read the next frame from the video
    ret, frame = cap.read()

    # Exit the loop if no frame is returned
    if not ret:
        break

    # Perform object detection on the current frame
    results = model(frame, conf=0.5)

    # Draw bounding boxes, labels, and confidence scores
    annotated_frame = results[0].plot()

    # Save the annotated frame to the output video
    out.write(annotated_frame)

    # Display the annotated frame
    cv2.imshow(
        "YOLO Video Detection",
        annotated_frame
    )

    # Press 'q' to stop the video processing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Release the video writer object
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

print("Video saved successfully.")