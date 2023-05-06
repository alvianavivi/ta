import cv2
import numpy as np
import os 
import mediapipe as mp

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/FaceRecog/trainer/trainer.yml')
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'zul', 'iwan', 'yoshi'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

face_detection = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)


while True:

    ret, img =cam.read()
    if not ret:
        print("kosong")
        continue

    img = cv2.flip(img, 1) # Flip vertically
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)

    if results.detections:
        for detection in results.detections:

            # Get the bounding box of the face
            bbox = detection.location_data.relative_bounding_box
            height, width, _ = img.shape
            x, y, w, h = int(bbox.xmin * width), int(bbox.ymin * height), int(bbox.width * width), int(bbox.height * height)

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

            face_img = img[y:y+h, x:x+w]
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

            id, confidence = recognizer.predict(face_img)

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
