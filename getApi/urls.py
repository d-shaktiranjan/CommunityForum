from django.urls import path
from getApi import views

urlpatterns = [
    path('', views.index, name="index"),
]
