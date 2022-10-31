from django.contrib import admin
from . import models



class TicketComment(admin.SimpleListFilter):
    models = models.File

@admin.register(models.Post)
class Post(admin.ModelAdmin):
    list_display = ("title", "image")
    list_filter = ("title", "image",)
    list_editable = ("image",)


admin.site.register(models.File)
