from django.shortcuts import render, redirect
from home.models import User
from django.views import View
from django.views.generic import ListView
from post.models import Post, File

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        body = request.POST.get('body')
        User.objects.create(name=name, email=email, topic=topic, body=body)
    articles = Post.objects.all()
    return render(request, "home/index.html", {"articles":articles})


class FileDownloadView(ListView):
    model = File
    fields = ['file']
    template_name = 'home/download.html'

