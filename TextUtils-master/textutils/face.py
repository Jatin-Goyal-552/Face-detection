# -*- coding: utf-8 -*-

from PIL import Image
import requests
from io import BytesIO   
import cv2
import numpy as np
import matplotlib.pyplot as plt

class facerecognition:
    def detectface(self,imglink):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        response = requests.get(imglink)
        img = Image.open(BytesIO(response.content))
        img=np.array(img)
        print(img)
        faces = face_cascade.detectMultiScale(img, 1.1, 4)
        for (x, y, w, h) in faces: 
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print(x)
        print(y)
        print(w)
        print(h)
        data = Image.fromarray(img) 
      
    # saving the final output  
    # as a PNG file 
        data.save('static/media/a.png')
        return data