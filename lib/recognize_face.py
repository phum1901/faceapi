import face_recognition

def recognizeFace(image):
    if image is None:
        return None
    face_encoding = face_recognition.face_encodings(image)[0]
    output = {}
    output['vector'] = face_encoding
    return output

