import cv2

img1 = cv2.imread(r'T:\imgs\XL4\a.png')
img2 = cv2.imread(r'T:\imgs\XL4\b.png')

a,b = int(img1.shape[1]/4),int(img1.shape[0]/4)
img1 = cv2.resize(img1,(a,b))

a,b = int(img2.shape[1]/4),int(img2.shape[0]/4)
img2 = cv2.resize(img2,(a,b))

cv2.imwrite(r'T:\imgs\XL4\klcc_a.png',img1)
cv2.imwrite(r'T:\imgs\XL4\klcc_b.png',img2)