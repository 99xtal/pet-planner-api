from django.urls import path
from pingpong import views

urlpatterns = [
    path("", views.ping),
]


