from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("posts/earthrise/", views.post, name="post"),
]
