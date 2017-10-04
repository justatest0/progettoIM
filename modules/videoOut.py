import cv2
import modules.parser as parser

def showVideo(windowsName, frame):
    cv2.imshow(windowsName, frame)

def createVideoOutput(frame, fps):
    h = frame.shape[0]
    w = frame.shape[1]

    #Set the name of the output file
    if parser.outputVideo is 'E64E093307615569593609618F2FBBC53A28A59452D156F8D8827B465289B18C':
        nameFile = time.time()
    else:
        nameFile = parser.outputVideo

    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter('%s.mp4' %str(nameFile), fourcc, fps, (w, h), True)

    return out


def saveVideo(out, frame):
    out.write(frame)
