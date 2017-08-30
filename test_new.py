import cv2 
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
# capture frames from a camera
cap = cv2.VideoCapture()
 
ret, img = cap.read() 
 
#convert to gray scale of each frames
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Detects faces of different sizes in the input image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
for (x,y,w,h) in faces:
    # To draw a rectangle in a face 
    cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,0),2) 
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
 
cv2.imwrite('result_fave.jpg', gray)

# Display an image in a window
cv2.imshow('img',gray)
			
cv2.imwrite('result.jpg', gray)
 
# Close the window
cap.release()
 
# De-allocate any associated memory usage
cv2.destroyAllWindows() 