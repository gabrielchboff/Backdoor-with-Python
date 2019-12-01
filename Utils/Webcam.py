

#TODO html file send email

class MyClass:
  
    def get_webcam():
        import cv2
        import sys

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('webcam_get', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()