from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("poeme-1/", views.poeme1, name="poeme1"),
    path("poeme-2/", views.poeme2, name="poeme2"),
    path("poeme-3/", views.poeme3, name="poeme3"),
    path("poeme-4/", views.poeme4, name="poeme4"),
    path("poeme-5/", views.poeme5, name="poeme5"),
    path("poeme-6/", views.poeme6, name="poeme6"),
    path("message/", views.message, name="message"),
]