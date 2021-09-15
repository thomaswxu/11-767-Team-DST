Lab 0: Hardware setup
===
The goal of this lab is for you to become more familiar with the hardware platform you will be working with this semester, and for you to complete basic setup so that everyone in the group should be able to work remotely on the device going forward. By the end of class today, everyone in your group should be able to ssh in to the device, use the camera to take a picture, record audio, run a basic NLP model, and run a basic CV model. 

If you successfully complete all those tasks, then your final task is to write a script that pipes together I/O with a model. For example, you could write a script that uses the camera to capture an image, then runs classification on that image. Or you could capture audio, run speech-to-text, then run sentiment analysis on that text.

**Group name: DST**
---
Group members present in lab today: Thomas Xu, Dhruv Naik, Saloni Mittal

1: Set up your device.
----
Depending on your hardware, follow the instructions provided in this directory: [Raspberry Pi 4](https://github.com/strubell/11-767/blob/main/labs/lab0-setup/setup-rpi4.md), [Jetson Nano](https://github.com/strubell/11-767/blob/main/labs/lab0-setup/setup-jetson.md), [Google Coral](https://coral.ai/docs/dev-board/get-started/). 
1. What device(s) are you setting up?  
> Jetson Nano (2GB)  

2. Did you run into any roadblocks following the instructions? What happened, and what did you do to fix the problem?  
~~~
 30 min/stuck on first boot (fixed by re-plugging and unplugging keyboard)
SSH Permission denied (fixed by using "dst-nano" as user instead of "ubuntu")

 pip wasn't working in a miniconda environment (core dumped error)
 Uninstalled  miniconda and created the environment using venv instead.
~~~ 

3. Are all group members now able to ssh in to the device from their laptops? If not, why not? How will this be resolved?
> Yes, all members are able to ssh into the Jetson.

2: Collaboration / hardware management plan
----
4. What is your group's hardware management plan? For example: Where will the device(s) be stored throughout the semester? What will happen if a device needs physical restart or debugging? What will happen in the case of COVID lockdown?  

> The device is currently stored in the NSH Basement (B506) lab. If the device needs a physical restart or debugging, Tom will go to the lab. In case of a COVID lockdown, the device will be stored at the team's personal apartments. 


3: Putting it all together
----
5. Now, you should be able to take a picture, record audio, run a basic computer vision model, and run a basic NLP model. Now, write a script that pipes I/O to models. For example, write a script that takes a picture then runs a detection model on that image, and/or write a script that runs speech-to-text on audio, then performs classification on the resulting text. Include the script at the end of your lab report.

6. Describe what the script you wrote does (document it.)  
~~~
 The script we wrote uses the camera module to take an image, and then runs a simple facial recognition function (from OpenCV) to draw a bounding box around any detected faces.  
~~~
7. Did you have any trouble getting this running? If so, describe what difficulties you ran into, and how you tried to resolve them.

~~~
Camera wasn't being detected. We had to replug it into the connector, and were successful in locking the CSI latch properly.
Had to downgrade numpy to 1.19.4 as it was causing the illegal core dump error.
Changed default sound device for the sounddevice package in capture_audio.py

Got opencv working with the .whl file shared on Slack.
Couldn't detect faces with a face mask, but it worked perfectly without a mask on.
~~~
---
### Face Detection Script
```python
  
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
```
