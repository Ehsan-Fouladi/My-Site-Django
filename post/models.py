from django.db import models





class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to="images/Post", verbose_name='عکس')


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"


class File(models.Model):
    file = models.FileField(upload_to='documents', verbose_name='فایل' )

    def __str__(self):
        return f'{self.file}'

    class Meta:
        verbose_name = "دانلود"
        verbose_name_plural = "دانلود ها"
