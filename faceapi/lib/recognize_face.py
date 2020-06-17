import face_recognition

def recognizeFace(image):
    if image is None:
        return None
    face_encoding = face_recognition.face_encodings(image)[0]
    output = {}
    output['vector'] = face_encoding
    return output
if __name__ == '__main__':
    path = r'C:\Users\user\AI_group\data1\without_mask\0.jpg'
    vector = recognizeFace(path)
