import cv2
import numpy as np
from PIL import Image
import os
import mediapipe as mp
import numpy as np

# Path for face image database
path = '/home/pi/FaceRecog/dataset'

width=100
height=100

recognizer = cv2.face.LBPHFaceRecognizer_create()
mp_face_detection = mp.solutions.face_detection
face_detector = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
face_mesh = mp.solutions.face_mesh.FaceMesh()

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        #image = cv2.imread(imagePath)
        #image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results_detection = face_detector.process(image_numpy)
        detections = results_detection.detections

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        #faces = detector.process(img_numpy)

        for detection in faces.detections:
            bbox = detection.location_data.relative_bounding_box
            x, y, w, h = int(bbox.xmin * width), int(bbox.ymin * height), int(bbox.width * width), int(bbox.height * height)
            
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('/home/pi/FaceRecog/trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
