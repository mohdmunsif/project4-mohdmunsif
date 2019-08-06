from django.urls import path

from . import views

app_name = 'entries'

urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("browse", views.browse, name="browse")
]
