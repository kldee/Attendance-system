import cv2

# Read the image
image = cv2.imread("Rocky.jpg")

height, width = image.shape[:2]
new_width = int(width / 8)
new_height = int(height / 8)

resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

cv2.imshow("Resized Image", resized_image)
close allwindows
