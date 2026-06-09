# YOLO-Object-Detection
Image, video and webcam object detection using Ultralytics YOLO and OpenCV.

# YOLO Object Detection using Ultralytics and OpenCV

This repository demonstrates object detection using **Ultralytics YOLO11** and **OpenCV**. The project covers image detection, video detection, and real-time webcam detection.

## Features

* **Image Object Detection**

  * Detect objects in static images.
  * Display the detection results.
  * Save the annotated image.

* **Video Object Detection**

  * Perform frame-by-frame object detection on videos.
  * Display the processed video.
  * Save the annotated output video.

* **Real-Time Webcam Detection**

  * Detect objects using a live webcam feed.
  * Display the detections in real time.

## Project Structure

```text
YOLO-Object-Detection/
│
├── Image_Testing/
│   ├── test.jpg
│   ├── Output/
│   │   └── detected_image.jpg
│   └── image_detection.py
│
├── Video_Testing/
│   ├── samples_data_vtest.avi
│   ├── Output/
│   └── video_detection.py
│
├── Webcam_Testing/
│   └── webcam_detection.py
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* OpenCV
* Ultralytics YOLO11
* PyTorch

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/YOLO-Object-Detection.git
cd YOLO-Object-Detection
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Programs

### Image Detection

```bash
python Image_Testing/image_detection.py
```

### Video Detection

```bash
python Video_Testing/video_detection.py
```

### Webcam Detection

```bash
python Webcam_Testing/webcam_detection.py
```

## Sample Applications

* Surveillance and security systems
* Traffic monitoring
* Industrial automation
* Robotics and autonomous systems
* Real-time object detection projects

## Learning Outcomes

Through this project, the following concepts were explored:

* Object Detection Fundamentals
* Working with Ultralytics YOLO
* Image Processing using OpenCV
* Real-Time Video Processing
* Saving and visualizing detection outputs
* Building a structured computer vision project

## Author

Harsh Tharani
