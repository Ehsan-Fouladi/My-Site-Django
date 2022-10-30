from re import T
from django.db import models
import django.utils.timezone



class User(models.Model):
    name = models.CharField(max_length=90, blank=True, verbose_name = "نام")
    email = models.EmailField(max_length=100, blank=True, verbose_name = "ایمیل")
    topic = models.CharField(max_length=80, blank=False, verbose_name = "موضوع")
    body = models.TextField(max_length=500, blank=True, verbose_name = "پیام")
    view_Time = models.DateTimeField(null=True, blank=False, default=django.utils.timezone.now)



    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"

