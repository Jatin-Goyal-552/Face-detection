# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls import include, url
from textutils.face import facerecognition
from PIL import Image
from django.http import FileResponse
#from . import haarcascade_frontalface_alt2
def index(request):
    return render(request, 'index.html')

facerecognition=facerecognition()

def result(request):
    imglink=request.GET.get('text','default')
    print(imglink)
    img=facerecognition.detectface(imglink)
    #img=img.flatten()
    #params={"image":img}
    #image_data = open("C:/Users/dell/TextUtils-master/TextUtils-master/static/a.png", "rb").read()
    #return HttpResponse(image_data, content_type="image/png")
    #return render(request, 'result.html')
    return render(request,'result.html')
    #return HttpResponse(img)