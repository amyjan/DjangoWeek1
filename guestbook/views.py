"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrub.auth.models import User
from guestbook.models import TextMessage

def home(request):
	t1 = TextMessage.objects.create(talker='Michael', message='Hello')

	msgs = TextMessage.objects.all()

	return render(request,'guestbook')

def post(request):
        if request.method == 'POST':
                form = MessageForm(request.POST)
                if form.is_valid():
                        message = Message(t1=form.cleaned_data['t1'],msgs=form.cleaned_data['msgs'])
                        message.save()
                        return redirect('/board')
        else:
                form = MessageForm()
        return render_to_response('week2.html',{'form': form}, context_instance=RequestContext(request))""
"""
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})