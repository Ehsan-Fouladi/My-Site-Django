from django.contrib import admin
from . import models



class TicketComment(admin.SimpleListFilter):
    models = models.File

@admin.register(models.Post)
class Post(admin.ModelAdmin):
    list_display = ("title", "show_image")
    list_filter = ("title",)
    search_fields = ("title",)
    list_per_page = 5


admin.site.register(models.File)
