import cv2
import numpy as np
from PIL import Image
import os
import mediapipe as mp
import numpy as np

# Path for face image database
path = '/home/pi/FaceRecog/dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection
face_detector = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
face_mesh = mp.solutions.face_mesh.FaceMesh()

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        image = cv2.imread(imagePath)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results_detection = face_detector.process(image_rgb)
        detections = results_detection.detections
        if detections is not None:
            for detection in detections:
                mp_drawing.draw_detection(image, detection)
            results_mesh = face_mesh.process(image_rgb)
            multi_face_landmarks = results_mesh.multi_face_landmarks
            if multi_face_landmarks is not None:
                for face_landmarks in multi_face_landmarks:
                    landmarks = []
                    for landmark in face_landmarks.landmark:
                        landmarks.append(landmark.x)
                        landmarks.append(landmark.y)
                        landmarks.append(landmark.z)
                    landmarks = np.array(landmarks, dtype=np.float32)
                    faceSamples.append(landmarks)

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        ids.append(id)
        
    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('/home/pi/FaceRecog/trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
