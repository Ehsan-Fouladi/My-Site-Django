from django.db import models
import django.utils.timezone
from django.utils.translation import gettext_lazy as _


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


class MySocialNetworks(models.Model):
    instagram = models.CharField(_("instagram"), max_length=500, blank=True, null=True)
    linkedin = models.CharField(_("linkedin"), max_length=500, blank=True, null=True)
    github = models.CharField(_("github"), max_length=500, blank=True, null=True)
    telegram = models.CharField(_("telegram"), max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "شبکه های من"
        verbose_name_plural = "شبکه های من"

    def __str__(self):
        return self.github
    
class Cv(models.Model):
    cv = models.TextField(_("cv"))

    class Meta:
        verbose_name = "درباره من"
        verbose_name_plural = "درباره من"

    def __str__(self):
        return self.cv[:20]