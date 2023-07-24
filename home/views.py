from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages
from post.models import Post, File
from .forms import ContactForms
from .models import MySocialNetworks, Cv

class ContactUserView(FormView):
    form_class = ContactForms
    template_name = "home/index.html"
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Post.objects.all()
        context["myNetwork"] = MySocialNetworks.objects.all()
        context["cvs"] = Cv.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, ".پیام شما با موفقیت ثبت شد!")
        return super().form_valid(form)

class FileDownloadView(ListView):
    model = File
    fields = ['file']
    template_name = 'home/download.html'