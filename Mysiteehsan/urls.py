from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from admin_notification.views import check_notification_view
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path('check/notification', check_notification_view, name="check_notifications"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
