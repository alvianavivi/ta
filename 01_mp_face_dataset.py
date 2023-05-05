import cv2
import os
import mediapipe as mp
import numpy as np

face_detection = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
landmark_detection = mp.solutions.face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)
cap.set(3, 640) # set video width
cap.set(4, 480) # set video height

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFOO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    success, image = cap.read()
    if not success:
        break

    # Convert image to RGB format and detect faces
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)


    if results.detections:
        dir_path = '/home/pi/FaceRecog/dataset/User' + str(face_id)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        for detection in results.detections:

            # Get the bounding box of the face
            bbox = detection.location_data.relative_bounding_box
            height, width, _ = image.shape
            x, y, w, h = int(bbox.xmin * width), int(bbox.ymin * height), int(bbox.width * width), int(bbox.height * height)

            cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
            # Crop the face region and convert it to RGB
            face_img = image[y:y+h, x:x+w]
            

            # Run face mesh on the cropped face image
            #face_results = mp_mesh.process(face_img_rgb)
            #landmarks = face_results.multi_face_landmarks     
            
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite('/home/pi/FaceRecog/dataset/User' + str(face_id) + '/' + str(count) + ".jpg", face_img)

            cv2.imshow('image', image)

        k = cv2.waitKey(100) & 0xff # Press 'ESC2' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 50 face sample and stop video
            break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cap.release()
cv2.destroyAllWindows()



