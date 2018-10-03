from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random


#def index(request):
#	return render(request, 'week2.html')


def home (request):
	base = "https://picsum.photos/200/200?image="
	ran = random.sample(range(1,100),10)
	images = [base+str(ran[i]) for i in range(len(ran))]
	
	return render(request,'week2.html',{'images':images})
