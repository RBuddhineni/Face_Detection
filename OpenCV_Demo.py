#This code is is simply a demo code to test the OpenCV python package.
#I used this code to test the webcam in order to implement it into the face detection model.

import cv2

# Open the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame was captured correctly
    if ret:
        # Display the resulting frame
        cv2.imshow('Live Webcam Feed', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
