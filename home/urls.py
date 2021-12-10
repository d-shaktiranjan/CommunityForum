from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('postQuestion', views.postQuestion, name="postQuestion"),
    path('logout', views.logout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('loginSignup', views.loginSignup, name="loginSignup"),
    path('postView', views.postView, name="postView"),
    path('addLike', views.addLike, name="addLike"),
    path('addDisLike', views.addDisLike, name="addDisLike"),
]
