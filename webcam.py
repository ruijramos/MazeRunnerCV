import numpy as np
import cv2

cap = cv2.VideoCapture(0)

maxheight = 480
maxWidth = 640

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# draw triangle 1
	vertices1 = np.array([[0, 0], [640, 0], [320, 240]], np.int32)
	pts1 = vertices1.reshape((-1, 1, 2))
	cv2.polylines(frame, [pts1], isClosed=True, color=(50,205,50), thickness=5)

	# draw triangle 2
	vertices2 = np.array([[0, 0], [0, 480], [320, 240]], np.int32)
	pts2 = vertices2.reshape((-1, 1, 2))
	cv2.polylines(frame, [pts2], isClosed=True, color=(180,105,255), thickness=5)

	# draw triangle 3
	vertices3 = np.array([[640, 0], [640, 480], [320, 240]], np.int32)
	pts3 = vertices3.reshape((-1, 1, 2))
	cv2.polylines(frame, [pts3], isClosed=True, color=(0, 0, 255), thickness=5)

	# draw triangle 4
	vertices4 = np.array([[0, 480], [640, 480], [320, 240]], np.int32)
	pts4 = vertices4.reshape((-1, 1, 2))
	cv2.polylines(frame, [pts4], isClosed=True, color=(255,0,0), thickness=5)

	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()