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
mp_drawing = mp.solutions.drawing_utils

mp_face_mesh = mp.solutions.face_mesh

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    face_encodings_dict = {}

    for imagePath in imagePaths:

        #PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        #img_numpy = np.array(PIL_img,'uint8')

        image = cv2.imread(imagePath)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        results_detection = face_detector.process(image_gray)
        detections = results_detection.detections

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        #faces = detector.process(img_numpy)

        for detection in detections:
            bbox = mp_drawing._normalized_to_absolute_bounding_box(detection.location_data.relative_bounding_box, image.shape[1], image.shape[0])
            face = image_gray[int(bbox[1]):int(bbox[1]+bbox[3]), int(bbox[0]):int(bbox[0]+bbox[2])]
            
            # Extract the facial landmarks using the Face Mesh model in MediaPipe
            with mp_face_mesh.FaceMesh(max_num_faces=1) as face_mesh:
                results_mesh = face_mesh.process(face)
                face_landmarks = results_mesh.multi_face_landmarks[0]
            # Convert the landmarks to a numpy array and add it to the list of face encodings for this person
            face_encoding = np.array([(landmark.x, landmark.y) for landmark in face_landmarks.landmark]).flatten()
            if id in face_encodings_dict:
                face_encodings_dict[id].append(face_encoding)
            else:
                face_encodings_dict[id] = [face_encoding] 

            ids.append(id)

    return face_encodings_dict

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces = getImagesAndLabels(path)
face_encodings = []
labels = []
for person_name, person_face_encodings in faces.items():
    face_encodings.extend(person_face_encodings)
    labels.extend([person_name]*len(person_face_encodings))
recognizer.train(face_encodings, np.array(labels))

# Save the model into trainer/trainer.yml
recognizer.write('/home/pi/FaceRecog/trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
