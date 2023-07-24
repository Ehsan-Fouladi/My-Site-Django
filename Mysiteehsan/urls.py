from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from admin_notification.views import check_notification_view
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path('check/notification', check_notification_view, name="check_notifications"),
    re_path(r'^rosetta/', include('rosetta.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
