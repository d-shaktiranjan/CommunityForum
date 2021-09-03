from django.urls import path
from postApi import views

urlpatterns = [
    path('', views.index, name="index3"),
]
