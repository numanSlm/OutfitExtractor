# Outfit Extractor

This project aims to extract outfits from images or live video streams using MediaPipe, OpenCV, and Python. It detects human poses and uses the detected landmarks to outline the person's body, enabling the extraction of outfits.

## Dependencies

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- NumPy
- Matplotlib

## Installation

Install the required dependencies using pip:

```bash
pip install opencv-python mediapipe matplotlib numpy
```
## Usage

### Outfit Extractor from Images
The outfit-extractor.ipynb notebook contains code to extract outfits from images. It works as follows:

1. Load an image.
2. Use MediaPipe Pose to detect landmarks on the person's body.
3. Calculate the bounding box around the person's body based on detected landmarks.
4. Use GrabCut algorithm to segment the person's body from the background.
5. Display the extracted outfit.

### Outfit Extractor from Live Video(WIP) 
The outfit.py script extracts outfits from live video streams. Here's how it works:

1. Capture video frames from the webcam.
2. Process each frame to detect poses using MediaPipe Pose.
3. Draw landmarks on the detected poses.
4. Calculate the bounding box around the person's body based on detected landmarks.
5. Display the live video with extracted outfits in real-time.

### Code Synopsis
##### outfit-extractor.ipynb

The notebook starts by importing necessary libraries such as OpenCV, MediaPipe, NumPy, and Matplotlib.

It initializes MediaPipe Pose for static image processing and sets confidence thresholds.

Pose landmarks are detected on the loaded image.

Bounding box coordinates are calculated based on specific landmarks (e.g., shoulders, hips, elbows, ankles).

The outfit is extracted using the GrabCut algorithm.

The process is visualized by drawing landmarks and bounding boxes on the original image.

##### outfit.py

The script captures frames from the webcam using OpenCV.

MediaPipe Pose is used to detect poses in each frame.

Landmarks are drawn on the detected poses.

Bounding box coordinates are calculated based on specific landmarks.

The live video is displayed with extracted outfits in real-time. (throws TF error)

