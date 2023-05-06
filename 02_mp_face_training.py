import cv2
import os
import mediapipe as mp
import numpy as np

# Path for face image database
path = '/home/pi/FaceRecog/dataset'

width=300
height=300

recognizer = cv2.face.LBPHFaceRecognizer_create()
mp_face_detection = mp.solutions.face_detection
face_detector = mp.solutions.face_detection.FaceDetection()
mp_drawing = mp.solutions.drawing_utils

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        
        image = cv2.imread(imagePath)
        results_detection = face_detector.process(image)

        if not results_detection.detections:
            continue

        for detection in results_detection.detections:
            bbox = detection.location_data.relative_bounding_box
            x, y, w, h = int(bbox.xmin * width), int(bbox.ymin * height), int(bbox.width * width), int(bbox.height * height) 
            face_img = image[y:y+h, x:x+w]

            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
            faceSamples.append(face_img)
            ids.append(id)

    return faceSamples, ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('/home/pi/FaceRecog/trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
