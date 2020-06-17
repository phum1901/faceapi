# import matplotlib.pyplot as plt
import pickle

from faceapi.lib.detect_face import detectFace
from faceapi.lib.recognize_face import recognizeFace

class ConvertFile:
    def __init__(self,image):
        self.__image        = image
        self.__face         = None
        self.__landmark     = None
        self.__encode       = None

        self.__detectFace   = None

        self.__face_binary        = None
        self.__landmark_binary    = None
        self.__encode_binary      = None

    def getFace(self):
        if detectFace(self.__image) == 'NO FACE':
            return 'NO FACE'
        # else:
        #     self.__detectFace   = detectFace(self.__image)['crop_image']
        #     self.__face_binary  = pickle.dumps(self.__detectFace)
        #     return self.__face_binary
    def getEncode(self):

        encode          = recognizeFace(self.__detectFace)['vector']
        self.__encode_binary  = pickle.dumps(encode)
        return self.__encode_binary
    def getLandmarkFace(self):
        landmark         = detectFace(self.__image)['landmark']
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


# if __name__ == '__main__':
#     from cv2 import imread
#     path = r'image\image.jpg'
#     image = imread(path)
#     ai   = ConvertFile(path)
#     face_B = ai.getFace()
#     landmark_B = ai.getLandmarkFace()
#     vec_B  = ai.getEncode()
#     face = ai.setFace(face_B)
#     landmark = ai.setLandmarkFace(landmark_B)
#     vec = ai.setEncode(vec_B)
#     plt.figure()
#     plt.imshow(face)
#     plt.figure()
#     plt.imshow(landmark)

import cv2
image = cv2.imread('yoda.jpg')
ai   = ConvertFile(image)
face_B = ai.getFace()

