"""import cv2

logo = cv2.imread("tenor.gif")

while True:
	cv2.imshow("logo", logo)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
"""
import cv2
import imageio

gif = imageio.mimread("bot_gif.gif")
nums = len(gif)
print("Total {} frames in the gif!".format(nums))

# convert form RGB to BGR 
imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]

## Display the gif
i = 0

while True:
    cv2.imshow("gif", imgs[i])
    if cv2.waitKey(100)&0xFF == 27:
        break
    i = (i+1)%nums
cv2.destroyAllWindows()
