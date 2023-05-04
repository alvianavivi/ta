import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Read an image and convert it to RGB
image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Run Mediapipe on the image to get the pose landmarks
with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
    results = pose.process(image)

    # Visualize the landmarks on the image
    image_landmarks = image.copy()
    mp_drawing.draw_landmarks(image_landmarks, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the image with landmarks
    cv2.imshow('image', image_landmarks)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


