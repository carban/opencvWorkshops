#LAUGHTING MAN
import cv2
import imageio
import pyfakewebcam

cap = cv2.VideoCapture(0)

fake1 = pyfakewebcam.FakeWebcam('/dev/video1', 640, 480)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#frame = cv2.imread("image.jpg")

smile = imageio.mimread("la.gif")
smile_length = len(smile)
# convert form RGB to BGR 
#smile_frames = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in smile]
smile_frames = [img for img in smile]
i = 0

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, 1.7, 5) #1.7 5
	
	for (x, y, w, h) in faces:
		#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		img2 = cv2.resize(smile_frames[i], (w, h))
		img1 = frame[y:(y+h), x:(x+w)];
		#merge = cv2.addWeighted(img1, 1, img2, 1, 1)
		
		alpha = img2[:, :, 3]                                       # Save alpha channel for later use
		_, alpha = cv2.threshold(alpha, 5, 255, cv2.THRESH_BINARY)    # Threshold alpha channel to prevent gradual transparency
		img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)                 # Remove alpha channel information, so that code below still works

		rows, cols, channels = img2.shape
		roi = img1[0:rows, 0:cols ]

                                                            # img2gray no longer needed
		mask = alpha                                                # Mask is just the alpha channel saved above
		mask_inv = cv2.bitwise_not(mask)

		img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

		img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

		dst = cv2.add(img1_bg, img2_fg)		
		
		frame[y:(y+h), x:(x+w)] = dst
	
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	#cv2.imshow('frame', frame)
	fake1.schedule_frame(frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
	i = (i + 1) % smile_length


cap.release()
cv2.destroyAllWindows()
