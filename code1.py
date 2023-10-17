import cv2 

video = cv2.VideoCapture(0)

while True:

    success, frame = video.read()
    if success:
        cv2.imshow("WEBCAM", frame)
    
    if cv2.waitKey(2)==32:
        break