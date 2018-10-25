from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random
#

#def index(request):
#	return render(request, 'week2.html')


#def home(request):
#	base = "https://picsum.photos/200/200?image="
#	ran = random.sample(range(1,100),10)
#	images = [base+str(ran[i]) for i in range(len(ran))]
	
#	return render(request,'week2.html',{'images':images})


#from django.shortcuts import render, redirect
#rom django.contrib.auth import authenticate
#from django.http import HttpResponse
#from django.contrub.auth.models import User
#from guestbook.models import TextMessage
"""
def home(request):
	t1 = TextMessage.objects.create(talker='Michael', message='Hello')

	msgs = TextMessage.objects.all()

	return render(request,'week2.html',{'msgs':msgs})
"""
from django.shortcuts import render, get_object_or_404

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

 def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})