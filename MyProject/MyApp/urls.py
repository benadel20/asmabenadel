from django.urls import path, include
from .import views
from django.contrib import admin
from .views import facebook_callback


urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path('auth/facebook/callback/', facebook_callback, name='facebook_callback'),
    path('', include('social_django.urls', namespace='social')), 
    path("login/", views.login_view, name="login"),
    path("success/", views.success, name="success"),

]

