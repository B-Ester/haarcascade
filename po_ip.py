import cv2 
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
# Trained XML file for detecting eyes
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
 
# capture frames from a camera
cap = cv2.VideoCapture(1)

if cap.isOpened():
	ret, img = cap.read() 
 
    # convert to gray scale of each frames
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    # Detects faces of different sizes in the input image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
	for (x,y,w,h) in faces:
    # To draw a rectangle in a face 
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
    	roi_gray = gray[y:y+h, x:x+w]
    	roi_color = img[y:y+h, x:x+w]
   
    # Display an image in a window
	cv2.imshow('img',img)

    # Write file
	cv2.imwrite('result.jpg', img)
 
	# Close the window
	cap.release()
 
	# De-allocate any associated memory usage
	cv2.destroyAllWindows() 
else:
	print('Camera is closed')