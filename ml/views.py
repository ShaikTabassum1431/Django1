from django.shortcuts import render,redirect
from sklearn.preprocessing import StandardScaler
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import os
import io
from transformers import pipeline
import torch
# Create your views here.
def ml_p(request):
    result=None
    if request.method=="POST":
        filename='diabetics.pkl'
        load_model=pickle.load(open(filename,'rb'))
        p=int(request.POST.get('p')) 
        g=int(request.POST.get('g')) 
        B=int(request.POST.get('B'))
        s=int(request.POST.get('s')) 
        i=int(request.POST.get('i'))
        b=float(request.POST.get('b')) 
        d=float(request.POST.get('d')) 
        a=int(request.POST.get('a'))
        result=p
        l=[] 
        l.append([p,g,B,s,i,b,d,a]) 
        sc=StandardScaler()
        l=sc.fit_transform(l) 
        ans=load_model.predict(l) 
        if ans[0]==0:
             result="NO" 
        else:
           result="YES"
        return render(request,'home.html',{'result':result})
    return render(request,'home.html')
def dl_p(request):
    model = load_model("brain_tumor_detection_model.h5")
    prediction=None 
    IMG_SIZE=(150,150)
    if request.method=='POST' and request.FILES.get('image'):
        uploaded_image=request.FILES['image']  
        img=image.load_img(io.BytesIO(uploaded_image.read()),target_size=IMG_SIZE)
        img_array=image.img_to_array(img) 
        img_array=np.expand_dims(img_array,axis=0) 
        img_array /=255.0 
        result=model.predict(img_array)[0]
        if result>0.5:
            prediction="Without Mask" 
        else:
            prediction="With Mask"
        return render(request,'dlhome.html',{'prediction':prediction})
    return render(request,'dlhome.html',{'prediction':prediction})
def ai(request):
    return render(request,'ai.html')
def ai_p(request):
    summarized=None
    if request.method=="POST":
        text=request.POST.get('text') 
        summarizer = pipeline("summarization")

        summary = summarizer(text, max_length=50, min_length=10, do_sample=False)

        summarized=summary[0]['summary_text']
        return render(request,'aihome.html',{'summarized':summarized})
    return render(request,'aihome.html')
def ai_question(request):
    answer=None
    if request.method=="POST":
        qa = pipeline("question-answering")
        context = request.POST.get('text')
        question =request.POST.get('que')
        answer = qa(question=question, context=context)
        answer=answer['answer']
        return render(request,'aiquestion.html',{'answer':answer})
    return render(request,'aiquestion.html')
def first(request):
    return render(request,'first.html') 
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('un')
        password = request.POST.get('ps')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('f') 
        else:
            return render(request, 'login.html', {'error': "Invalid username or password"})
    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        username = request.POST.get('un')
        password = request.POST.get('ps') 
        conpass = request.POST.get('ps1')
        if password != conpass:
            return render(request, 'register.html', {'error': "Passwords do not match"})
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "Username already exists"})
        user = User.objects.create_user(username=username, password=password)
        return redirect('l')
    return render(request,'register.html')