import cv2
import numpy as np
from PIL import Image
import os
import mediapipe as mp
import numpy as np

# Path for face image database
path = '/home/pi/FaceRecog/dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# Create list of images and corresponding labels
face_encodings = []
labels = []

# function to get the images and label data
def getImagesAndLabels(train_dir):

    for label in os.listdir(train_dir):
        label_path = os.path.join(train_dir, label)
        for img_path in os.listdir(label_path):
            image = cv2.imread(os.path.join(label_path, img_path))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
                results_detection = face_detection.process(gray)
                detections = results_detection.detections

                if detections is not None:
                    for detection in detections:
                        bbox = mp_drawing._normalized_to_absolute_bounding_box(detection.location_data.relative_bounding_box, image.shape[1], image.shape[0])
                        # Crop the face region
                        face = gray[int(bbox[1]):int(bbox[1]+bbox[3]), int(bbox[0]):int(bbox[0]+bbox[2])]
                        # Resize the face image to a fixed size (e.g. 100x100)
                        face = cv2.resize(face, (100, 100), interpolation=cv2.INTER_LINEAR)
                        # Extract the facial landmarks using the Face Mesh model in MediaPipe
                        with mp_face_mesh.FaceMesh(max_num_faces=1) as face_mesh:
                            results_mesh = face_mesh.process(face)
                            face_landmarks = results_mesh.multi_face_landmarks[0]
                        # Convert the landmarks to a numpy array and add it to the list of face encodings
                        face_encoding = np.array([(landmark.x, landmark.y) for landmark in face_landmarks.landmark]).flatten()
                        face_encodings.append(face_encoding)
                        # Add the label for this face image (e.g. name of the person in the image)
                        labels.append(img_path.split('.')[0])
        
    return face_encodings, labels

print
print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('/home/pi/FaceRecog/trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
