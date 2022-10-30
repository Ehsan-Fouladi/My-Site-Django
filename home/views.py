from django.shortcuts import render, redirect
from home.models import User
from django.views import View
from django.views.generic import TemplateView, ListView


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        body = request.POST.get('body')
        User.objects.create(name=name, email=email, topic=topic, body=body)

    return render(request, "home/index.html", {})


# class HomeView(TemplateView):
#     template_name = "home/index.html"
    
    

# class HomeModelView(ListView):
#     template_name = "home/index.html"
#     model = User
