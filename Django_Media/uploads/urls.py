from django.urls import path
from . import views


app_name = "uploads"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("<int:article_pk>/", views.detail, name="detail"),
    # path(""/ views.index, name="index"),
    path("<int:article_pk>/delete", views.delete, name="delete"),
]