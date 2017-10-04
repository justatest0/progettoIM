import modules.TCP as TCP
import socket
import modules.setup as setup
import modules.videoIn as videoIn
import modules.parser as parser
import cv2

frameNumber = setup.frameNumber
camera = videoIn.aquireVideo()

if parser.protocol == "TCP":
    print "Client ready"

    while camera.isOpened():
        grabbed, frame, frameNumber = videoIn.grabVideo(camera, frameNumber)
        if not grabbed:
            print "Can't load the video"
        else:
            flattedFrame = frame.flatten()
            stringedFrame = flattedFrame.tostring()

            # data = stringedFrame[0*768:(0+1)*768]
            # socket.send(data)


            for i in xrange(1200):
                data = stringedFrame[i*768:(i+1)*768]
                socket = TCP.setupClient()
                socket.send(data)
                socket.close

            # cv2.imshow("Video", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                socket.close
                break

    print "Client disconnected"
