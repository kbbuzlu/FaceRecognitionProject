import cv2
import faces

def live_face(img):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces.face_recognition_func(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
