from django.urls import path
from api import views

urlpatterns = [
    path('sendOTP', views.sendOTP, name="sendOTP"),
    path('verifyOTP', views.verifyOTP, name="verifyOTP"),
]
