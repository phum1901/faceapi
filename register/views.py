from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import data
from faceapi.lib.ConvertFileClass import ConvertFile
# from faceapi.lib import detect_face2,recognize_face
from django.http import HttpResponse
from rest_framework import status
# from rest_framework.response import Response
import numpy as np
import cv2
import pickle
# from faceapi.lib import compare_feature
from scipy.spatial import distance
import face_recognition
import json

@csrf_exempt
def regis(request):
    if request.method == "POST":
        if 'name' not in request.POST.keys():
            return HttpResponse('no name',status=400)
            # return Response('no name', status=status.HTTP_404_NOT_FOUND)
        if 'id_man' not in request.POST.keys():
            return HttpResponse('no id_man',status=400)
            # return Response('no id_man', status=status.HTTP_404_NOT_FOUND)
        if 'image' not in request.FILES.keys():
            return HttpResponse('no image',status=400)
            # return Response('no image', status=status.HTTP_404_NOT_FOUND)
        else:
            if data.objects.filter(id_man=request.POST['id_man']).exists():
                return HttpResponse('already exist',status=400)
                # return Response('already exist', status=status.HTTP_404_NOT_FOUND)
            else:
                # print(request.FILES["image"])
                raw = request.FILES["image"].read()
                print(type(raw))
                img = np.asarray(bytearray(raw), dtype="uint8")
                arr = cv2.imdecode(img, cv2.IMREAD_COLOR)
                face = detectFace(arr)
                # con = ConvertFile(arr)
                # face = con.getFace()
                if face != 'NO FACE':
                    # vec = con.getEncode()
                    face_bin = pickle.dumps(face['crop_image'])
                    if recognizeFace(face['crop_image']) is None:
                        return HttpResponse('No Face Detect',status=403)
                    vec = pickle.dumps(recognizeFace(face['crop_image'])['vector'])
                    add_data   = data(name=request.POST['name'],id_man=request.POST['id_man'],image=face_bin,vector=vec)
                    add_data.save()
                    return HttpResponse('Register Success',status=201)
                else:
                    return HttpResponse('No Face Detect',status=403)

# @csrf_exempt
# def verify(request):
#     if request.method == "POST":
@csrf_exempt
def verify(request):
    if request.method == "POST":
        if 'image' not in request.FILES.keys():
            return HttpResponse('no image',status=400)
        else:
            raw = request.FILES["image"].read()
            img = np.asarray(bytearray(raw), dtype="uint8")
            arr = cv2.imdecode(img, cv2.IMREAD_COLOR)
            # print(np.shape(arr))
            face = detectFace(arr)
            if face != 'NO FACE':
                vec_arr = recognizeFace(face['crop_image'])['vector']
            # con = ConvertFile(arr)
            # face = con.getFace()
            # vec = con.getEncode()
            # vec_arr = pickle.loads(vec)
            # print(type(vec))
                dis_min = 1
                record_dis = []
                for vec_ in data.objects.values_list('vector'):
                    vec_db = pickle.loads(vec_[0])
                    dis = compare_dis(vec_arr,vec_db)
                    id_ = data.objects.values_list('id').filter(vector=vec_[0])[0][0]
                    name_ = data.objects.values_list('name').filter(vector=vec_[0])[0][0]
                    id_man_ = data.objects.values_list('id_man').filter(vector=vec_[0])[0][0]
                    record_dis.append((id_,name_,id_man_,dis))
                    # if dis<dis_min:
                    #     dis_min = dis
                    #     if dis<=0.4:
                    #         print(type(vec_[0]))
                    #         print(data.objects.values_list('id').filter(vector=vec_[0])[0][0])
                    #         print(data.objects.values_list('name').filter(vector=vec_[0])[0][0])
                    #         print(data.objects.values_list('id_man').filter(vector=vec_[0])[0][0])
                record_dis.sort(key=lambda tup: tup[3])
                print(record_dis[0][3])
                if record_dis[0][3] < 0.5:
                    print(record_dis[0][1])
                    print(record_dis[0][2])
                    return HttpResponse(f'NAME : {record_dis[0][1]}\nID_MAN : {record_dis[0][2]}')

                return HttpResponse(f'UNKNOWN WITH DISTANCE {record_dis[0][3]}',status=200)
            else:
                return HttpResponse('No Face Detect',status=403)


@csrf_exempt
def delete(request):
    if request.method == "POST":
        id_man = request.POST['id_man']
        data.objects.get(id_man=id_man).delete()
        return HttpResponse('deleted',status=200)
@csrf_exempt
def getData(request):
    response_data = {}
    data_ = data.objects.values()
    for d in data_:
        response_temp = {}
        response_temp['name'] = d['name']
        response_temp['id_man'] = d['id_man']
        response_data[d['id']] = response_temp
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=200)



@csrf_exempt
def clear_db(request):
    if request.method == "DELETE":
        data.objects.all().delete()
        return HttpResponse('deleted all data')


def compare_cos(vector1,vector2):
    cossim = 1 - distance.cosine(vector1, vector2)
    return cossim

def compare_dis(vector1,vector2):
    eucdis = distance.euclidean(vector1, vector2)
    return eucdis

def detectFace(path):
    image = path
    face_location = face_recognition.face_locations(image)
    if len(face_location)==0:
        return 'NO FACE'
    else:
        y2,x2,y1,x1 = face_location[0]
        w = x2-x1
        h = y2-y2
        crop_image = image[y2:y1, x1:x2, :]
        landmark = cv2.rectangle(image.copy(),(x1,y2),(x1+w,y1+h),(0,255,0),3)
        output = {}
        output['landmark'] = landmark
        output['crop_image'] = crop_image
        return output
def recognizeFace(image):
    if image is None:
        return None
    face_encoding = face_recognition.face_encodings(image)
    if face_encoding == []:
        return None
    output = {}
    output['vector'] = face_encoding[0]
    return output



