#LAUGHTING MAN
import cv2
import imageio
import pyfakewebcam

cap = cv2.VideoCapture(0)

fake1 = pyfakewebcam.FakeWebcam('/dev/video1', 640, 480)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#frame = cv2.imread("image.jpg")

smile = imageio.mimread("smile.gif")
smile_length = len(smile)
# convert form RGB to BGR 
smile_frames = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in smile]

i = 0

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, 1.7, 5) #1.7 5
	
	for (x, y, w, h) in faces:
		#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		new_smile = cv2.resize(smile_frames[i], (w, h))
		frame[y:(y+h), x:(x+w)] = new_smile
	
	#cv2.imshow('frame', frame)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	fake1.schedule_frame(frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
	i = (i + 1) % smile_length


cap.release()
cv2.destroyAllWindows()
