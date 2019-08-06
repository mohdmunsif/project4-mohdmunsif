from django.urls import path
from django.conf.urls import include, url

from . import views

app_name = 'users'

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup")
]
