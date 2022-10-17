from django.urls import path
from . import views

app_name = "uploads"

urlpatterns = [
    path("create/", views.create, name="create"),
]