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
    path('postView/<slug:slug>', views.postView, name="postView"),
    path('deletePost/<slug:slug>', views.deletePost, name="deletePost"),
    path('deleteComment/<slug:slug>', views.deleteComment, name="deleteComment"),
    path('editPost/<slug:slug>', views.editPost, name="editPost"),
    path('fixPost/<slug:slug>', views.fixPost, name="fixPost"),
    path('addLike', views.addLike, name="addLike"),
    path('addDisLike', views.addDisLike, name="addDisLike"),
    path('postComment', views.postComment, name="postComment"),
]
