import cv2 
import mediapipe as mp 
import pyautogui

cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

index_y = 0

while True:
    _, video = cap.read()
    video = cv2.flip(video,1)
    rgb_video = cv2.cvtColor(video,cv2.COLOR_BGR2RGB)
    video_height, video_width, _ = video.shape
    output = hand_detector.process(rgb_video)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(video,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*video_width)
                y = int(landmark.y*video_height)
                if id==8:
                    cv2.circle(img=video,center=(x,y),radius=10,color=(0,255,255))
                    index_x = screen_width/video_width *x
                    index_y = screen_height/video_height *y
                    pyautogui.moveTo(index_x,index_y)
                if id==4:
                    cv2.circle(img=video,center=(x,y),radius=10,color=(0,255,255))
                    thum_x = screen_width/video_width *x
                    thum_y = screen_height/video_height *y
                    if abs(index_y - thum_y)<30:
                        print("click")
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Virtual Mouse',video)
    cv2.waitKey(1)


