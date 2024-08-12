import cv2 
import mediapipe as mp 

cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands()

while True:
    _, video = cap.read()
    rgb_video = cv2.cvtColor(video,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_video)
    hands = output.multi_hand_landmarks
    print(hands)
    cv2.imshow('Virtual Mouse',video)
    cv2.waitKey(1)


