import face_recognition
import cv2
import matplotlib.pyplot as plt

def detectFace(path=None):
    image = path
    # image = face_recognition.load_image_file(path)
    # face_encoding = face_recognition.face_encodings(image)[0]
    face_location = face_recognition.face_locations(image)[0]
    y2,x2,y1,x1 = face_location
    w = x2-x1
    h = y2-y2
    crop_image = image[y2:y1, x1:x2, :]
    landmark = cv2.rectangle(image.copy(),(x1,y2),(x1+w,y1+h),(0,255,0),3)
    output = {}
    output['landmark'] = landmark
    output['crop_image'] = crop_image
    return output
if __name__ == '__main__':
    path = r'image\image.jpg'
    img = detectFace(path)['crop_image']
    plt.imshow(img)