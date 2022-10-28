from django.shortcuts import render
from home.models import User


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        body = request.POST.get('body')
        view = request.POST.get('view')
        time = request.POST.get('time')
        User.objects.create(name=name, email=email, topic=topic, body=body, view=view, time=time)

    return render(request, "home/index.html")
