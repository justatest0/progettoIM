#The following 3 are needed in order to import a sibiling directory such as parser
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import modules.parser as parser
import cv2

def aquireVideo():
    if (parser.webcamInputIndex is not None):
        cameraIndex = parser.webcamInputIndex
        camera = cv2.VideoCapture(cameraIndex)
        return camera
    if ((parser.videoInputPath is None) and (parser.webcamInputIndex is None)):
        camera = cv2.VideoCapture(0)
        return camera

def grabVideo(camera, iteration):
    grabbed, frame = camera.read()
    iteration += 1
    return grabbed, frame, iteration

def getFps(camera):
    fps = camera.get(cv2.CAP_PROP_FPS)
    return fps

def setWebcamResolution(camera, w, h):
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
