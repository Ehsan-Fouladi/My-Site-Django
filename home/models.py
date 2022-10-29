from django.db import models
import django.utils.timezone



class User(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    title = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=5000, blank=True)
    view_Time = models.DateTimeField(null=True, blank=False, default=django.utils.timezone.now)



    def __str__(self):
        return f"{self.name}, {self.email}, {self.title},{self.body}"

