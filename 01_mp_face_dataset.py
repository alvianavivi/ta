import cv2
import os
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
mp_mesh = mp.solutions.face_mesh.FaceMesh()
cap=cv2.VideoCapture(0)
cap.set(3, 640) # set video width
cap.set(4, 480) # set video height

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cap.read()
    img2 = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    faces = mp_face.process(gray)

    if faces.detections:
        for detection in faces.detections:

            # Get the bounding box of the face
            bbox = detection.location_data.relative_bounding_box
            height, width, _ = img.shape
            x, y, w, h = int(bbox.xmin * width), int(bbox.ymin * height), int(bbox.width * width), int(bbox.height * height)

            # Crop the face region and convert it to RGB
            face_img = img[y:y+h, x:x+w]
            face_img_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

            # Run face mesh on the cropped face image
            face_results = mp_mesh.process(face_img_rgb)
            landmarks = face_results.multi_face_landmarks     
            
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite('/home/pi/FaceRecog/dataset/User.' + str(face_id) + '.' + str(count) + ".jpg", face_img_rgb)

            cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 50 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cap.release()
cv2.destroyAllWindows()



