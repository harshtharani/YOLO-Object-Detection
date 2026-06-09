from ultralytics import YOLO
import cv2
import time

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam")
    exit()

# For FPS calculation
prev_time = time.time()

while True:
    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Could not read frame")
        break

    # Run YOLO detection
    results = model(frame, conf=0.5)

    # Get annotated frame with boxes and labels
    annotated_frame = results[0].plot()

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # Count detected objects
    num_objects = len(results[0].boxes)

    # Display FPS
    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.2f}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display object count
    cv2.putText(
        annotated_frame,
        f"Objects: {num_objects}",
        (10, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    # Show output
    cv2.imshow(
        "YOLO Webcam Detection",
        annotated_frame
    )

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()