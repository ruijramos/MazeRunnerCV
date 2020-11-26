import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Colors: BGR

maxWidth = 640
maxheight = 480

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# flip
	frame = cv2.flip(frame, 180) 

	# rectangle LEFT
	rec1_pt1 = (20, 166)
	rec1_pt2 = (206, 312)
	rec1 = cv2.rectangle(frame, rec1_pt1, rec1_pt2, (180,105,255), 3)

	# rectangle RIGHT
	rec2_pt1 = (432, 166)
	rec2_pt2 = (622, 312)
	rec2 = cv2.rectangle(frame, rec2_pt1, rec2_pt2, (0,0,250), 3)

	# rectangle UP
	rec3_pt1 = (226, 10)
	rec3_pt2 = (412, 156)
	rec3 = cv2.rectangle(frame, rec3_pt1, rec3_pt2, (0,128,0), 3)

	# rectangle DOWN
	rec4_pt1 = (226, 324)
	rec4_pt2 = (412, 470)
	rec4 = cv2.rectangle(frame, rec4_pt1, rec4_pt2, (255,144,30), 3)

	# center circle
	center = (320, 240)
	radius = 60
	circle = cv2.circle(frame, center, radius, (255,255,255), thickness=3, lineType=8, shift=0) 

	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()