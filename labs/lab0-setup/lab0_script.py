import cv2, os, sys


def gstreamer_pipeline(capture_width=1280, capture_height=720, 
                       display_width=1280, display_height=720,
                       framerate=60, flip_method=0):
  return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        f"width=(int){capture_width}, height=(int){capture_height}, "
        f"format=(string)NV12, framerate=(fraction){framerate}/1 ! "
        f"nvvidconv flip-method={flip_method} ! "
        f"video/x-raw, width=(int){display_width}, height=(int){display_height}, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
    )

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# cam params
HEIGHT=1280
WIDTH=1920
center = (WIDTH / 2, HEIGHT / 2)
M = cv2.getRotationMatrix2D(center, 180, 1.0)

nano = True
if nano:
  print("nano")
  cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)


# Read the frame
_, img = cap.read()
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect the faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display
#cv2.imshow('img', img)

# Save image
cv2.imwrite('face_pic.png', img)


# Release the VideoCapture object
cap.release()
