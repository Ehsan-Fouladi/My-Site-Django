from django.contrib import admin
from . import models

# Register your models here.

class TicketComment(admin.SimpleListFilter):
    models = models.User

@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ("name", "email", "topic")
    list_filter = ("name", "email",)
    list_editable = ("topic",)


admin.site.register(models.MySocialNetworks)
admin.site.register(models.Cv)