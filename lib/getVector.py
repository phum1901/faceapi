from faceapi.lib.detect_face import detectFace
from faceapi.lib.recognize_face import recognizeFace

def get(image):
    face = detectFace(image)['crop_image']
    vector = recognizeFace(face)['vector']
    return vector