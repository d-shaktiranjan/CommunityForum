from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('postQuestion', views.postQuestion, name="postQuestion"),
    path('logout', views.logout, name="logout"),
]
