# import modules.setup as setup
import modules.TCP as TCP
import modules.parser as parser
import modules.setup as setup
import modules.videoOut as videoOut
import numpy as np
import sys
import cv2
import time


i = 0
j = 0
stringedFrame = ""
firstTimeVideo = True


if parser.protocol == "TCP":
    try:
        socket = TCP.setupServer()
        print "Server online"

        while True:
            connection, address = socket.accept()
            data = connection.recv(setup.bufferSize)
            if i%1200==0 and i!=0:
                flattedFrame = np.fromstring(stringedFrame, dtype=np.uint8)
                frame = flattedFrame.reshape(480,640,3)
                if (firstTimeVideo == True):
                    outputVideo = videoOut.createVideoOutput(frame, 20)
                    firstTimeVideo = False
                videoOut.saveVideo(outputVideo, frame)
                stringedFrame = ""
            connection.close()
            stringedFrame += (data)
            i+=1


    except ValueError:
        print "Server offline"
