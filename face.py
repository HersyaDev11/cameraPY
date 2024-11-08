
import cv2

cap = cv2.VideoCapture(0)


frames_width = int(cap.get(3))
frames_height = int(cap.get(4))


fourcc = cv2.VideoWriter_fourcc(*"MJPG")


out = cv2.VideoWriter("recording.avi", fourcc, 20.0, (frames_width, frames_height))

while True:
    
    ret, frame = cap.read()

    if ret == True:
       
        out.write(frame)

        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       
        cv2.imshow("frame", gray)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


cap.release()
out.release()
cv2.destroyAllWindows()