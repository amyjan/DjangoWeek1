##from guestbook.models import TextMessage

#admin.site.register(TextMessage)
# Register your models here.
from django.contrib import admin
from .models import Post
#from django import forms


admin.site.register(Post)