import numpy as np
import matplotlib.pyplot as plt
import pickle

from detect_face import detectFace
from recognize_face import recognizeFace

class Integrator:
    def __init__(self,path):
        self.__path         = path
        self.__face         = None
        self.__landmark     = None
        self.__encode       = None

        self.__detectFace   = None

        self.__face_binary        = None
        self.__landmark_binary    = None
        self.__encode_binary      = None
    def getFace(self):
        self.__detectFace   = detectFace(self.__path)['crop_image']
        self.__face_binary        = pickle.dumps(self.__detectFace)
        return self.__face_binary
    def getEncode(self):
        encode          = recognizeFace(self.__detectFace)['vector']
        self.__encode_binary  = pickle.dumps(encode)
        return self.__encode_binary
    def getLandmarkFace(self):
        landmark         = detectFace(self.__path)['landmark']
        self.__landmark_binary = pickle.dumps(landmark)
        return self.__landmark_binary
    def setFace(self,face_binary):
        self.__face = pickle.loads(face_binary)
        return self.__face
    def setEncode(self,encode_binary):
        self.__encode = pickle.loads(encode_binary)
        return self.__encode
    def setLandmarkFace(self,landmark_binary):
        self.__landmark = pickle.loads(landmark_binary)
        return self.__landmark

if __name__ == '__main__':
    path = r'image\image.jpg'
    ai   = Integrator(path)
    faceB = ai.getFace()
    landmarkB = ai.getLandmarkFace()
    vecB  = ai.getEncode()
    face = ai.setFace()
    landmark = ai.setLandmarkFace()
    vec = ai.setEncode()
    plt.figure()
    plt.imshow(face)
    plt.figure()
    plt.imshow(landmark)


