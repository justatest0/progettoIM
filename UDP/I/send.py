import numpy as np
import cv2
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

cap = cv2.VideoCapture(0)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while(True):
    ret, frame = cap.read()

    # cv2.imshow("Video", frame)

    d = frame.flatten()
    s = d.tostring()

    for i in xrange(20):
        data = s[i*46080:(i+1)*46080]
        data += str(i)
        sock.sendto(data, (UDP_IP, UDP_PORT))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()
cap.release()
cv2.destroyAllWindows()
