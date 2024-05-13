import cv2
import mediapipe as mp
import numpy as np
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)
pTime = 0

while True:
	success, img = cap.read()
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	results = pose.process(imgRGB)
	if results.pose_landmarks:
		mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
		for id, lm in enumerate(results.pose_landmarks.landmark):
			h,w,c = img.shape
			print(id, lm)
			cx, cy = int(lm.x*w), int(lm.y*h)
			cv2.circle(img, (cx, cy), 5, (255,0,0), cv2.FILLED)

			cv2.imshow("Image", img)
	cv2.waitKey(1)