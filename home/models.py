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
    
class Services(models.Model):
    img = models.ImageField(_("image"), upload_to="Services")
    title = models.CharField(_("title"), max_length=90)
    text = models.TextField(_("text"))
    time_ser = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural = "سروریس"

    def __str__(self):
        return self.title

class PlanPrice(models.Model):
    title =  models.CharField(max_length=90, verbose_name="پلن")
    subject = models.TextField(verbose_name="موضوع")
    support = models.CharField(max_length=90, verbose_name="پشتیبانی")
    price = models.CharField(max_length=90, verbose_name="قیمت")
    days = models.CharField(max_length=40, verbose_name="پلن چند روزه")
    proposal = models.BooleanField(default=False, null=True, blank=True, verbose_name="پیشنهاد")

    class Meta:
        verbose_name = "پلن"
        verbose_name_plural = "پلن قیمت"

    def __str__(self):
        return self.price
    
class experiences(models.Model):
    time_days = models.CharField(max_length=50, verbose_name="تاریخ")
    title = models.CharField(max_length=50, verbose_name="عنوان")
    subjects = models.TextField(verbose_name="موضوع")

    class Meta:
        verbose_name = "تجربه"
        verbose_name_plural = "تجربیات"

    def __str__(self):
        return self.title
    
class ExperiencesCores(models.Model):
    time_days = models.CharField(max_length=50, verbose_name="تاریخ")
    title = models.CharField(max_length=50, verbose_name="عنوان")
    subjects = models.TextField(verbose_name="موضوع")

    class Meta:
        verbose_name = "دانش"
        verbose_name_plural = "دانش من"

    def __str__(self):
        return self.title