from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render  
from django.http import HttpResponse  
from content.functions import handle_uploaded_file  
from content.forms import StudentForm 
import os
#from .mlmodels import MyRes
from keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage.transform import resize

from .forms import DocumentForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
os.system("python content/tests.py")
x = os.path.join(BASE_DIR, 'media\\documents')
y = os.path.join(BASE_DIR, 'content\\car2_final_model.h5')
print(x)
print(y)
model = load_model(y)

def load_image(file_path): 
    return cv2.imread(file_path)
test_path =x
ima_files = os.listdir(test_path)
print(ima_files)
test_images = [load_image(test_path + file) for file in ima_files]

my_image_resized =[] #resize the image to 32x32 pixel with depth = 3





file=open('content/data.txt','r')
rs=file.read()

file.close()
print(rs)
def home2(request):
   global BASE_DIR
   if request.method == "POST": 
      asd = handle_uploaded_file(request.FILES['file'])
      print( asd )

      #remove files from dir
      x = os.path.join(BASE_DIR, 'media\\documents')
      z = os.listdir(x)
      if len(z) > 0:
          for i in z :
            y  = os.path.join(x , i)
            os.remove(y)   
      #end remove   
 
      return render(request, 'result.html', {'test':rs})  
   else:
        
        x = os.path.join(BASE_DIR, 'media\\documents')
        print(os.listdir(x))
        return render(request, 'con_main.html', {})

 
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"test.html",{'form':student})  

def homeview(request):
    if request.method == 'POST':
        global rs
        print("inside this")
        form = DocumentForm(request.POST, request.FILES)
        print("inside 2")
        if form.is_valid():
            form.save()
            # model exection here
            # after getting model results, run remove images code

            return render(request, 'result.html', {'test':rs})  
    else:
        form = DocumentForm()
    return render(request, 'con_main.html', {
        'form': form
    })