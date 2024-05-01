from django.db import models
from django.utils.html import format_html

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to="images/Post", verbose_name='عکس')


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="110px" width="150px">')
        return format_html('<h3 style="color: red">تصویر موجود نیست</h3>')
    show_image.short_description = "عکس بند انگشتی"

class File(models.Model):
    file = models.FileField(upload_to='documents', verbose_name='فایل' )

    def __str__(self):
        return f'{self.file}'

    class Meta:
        verbose_name = "دانلود"
        verbose_name_plural = "دانلود ها"
