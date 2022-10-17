from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "uploads"

urlpatterns = [
    path("create/", views.create, name="create"),
] + static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)