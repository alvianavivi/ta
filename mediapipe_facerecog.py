import mediapipe as mp
import cv2
import numpy as np
import uuid

face_detection = mp.solutions.face_detection.FaceDetection()
landmark_detection = mp.solutions.face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while(True):
    success, image = cap.read()
    if not success:
        break

    # Convert image to RGB format and detect faces
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)

    # Loop through each detected face and detect landmarks
    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            h, w, _ = image.shape
            x1, y1, x2, y2 = int(bbox.xmin * w), int(bbox.ymin * h), int((bbox.xmin + bbox.width) * w), int((bbox.ymin + bbox.height) * h)
            face_image = image[y1:y2, x1:x2]
            landmarks = landmark_detection.process(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)).multi_face_landmarks[0]
            
            # Save the recognized face image to local storage
            cv2.imwrite('face_{}.jpg'.format(str(uuid.uuid4())), face_image)
            
            # Draw landmarks on the original image
            for lm in landmarks.landmark:
                x, y = int(lm.x * face_image.shape[1]), int(lm.y * face_image.shape[0])
                cv2.circle(face_image, (x, y), 2, (0, 255, 0), -1)
                cv2.putText(face_image, str(lm.z), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

            # Draw bounding box around the face
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display the output video
    cv2.imshow('image', image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

