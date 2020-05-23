import cv2 as cv

img1 = cv.imread('image.jpg')
img2 = cv.imread('laughting.png', cv.IMREAD_UNCHANGED)         # Added cv.IMREAD_UNCHANGED parameter to maintain alpha channel information

img2 = cv.resize(img2, (300, 300))

alpha = img2[:, :, 3]                                       # Save alpha channel for later use
_, alpha = cv.threshold(alpha, 5, 255, cv.THRESH_BINARY)    # Threshold alpha channel to prevent gradual transparency
img2 = cv.cvtColor(img2, cv.COLOR_BGRA2BGR)                 # Remove alpha channel information, so that code below still works

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols ]

                                                            # img2gray no longer needed
mask = alpha                                                # Mask is just the alpha channel saved above
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)

img2_fg = cv.bitwise_and(img2, img2, mask = mask)

dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
