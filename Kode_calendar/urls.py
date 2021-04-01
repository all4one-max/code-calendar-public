from django.urls import path

from django.contrib.auth import views as auth_views


from . import views  # from base import views

urlpatterns = [
    path("", views.home, name="home"),
    path("all/", views.all, name="all"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.register, name="register"),
    path("logoutUser/", views.logoutUser, name="logoutUser"),
    path('about/',views.about,name="about"),
    path('google_oauth/redirect/', views.RedirectOauthView_all ,name="oauth_all"),
    path('google_oauth/redirect/', views.RedirectOauthView_home ,name="oauth_home"),
    path('google_oauth/callback/',views.Callback),
    path('privacy_policy/',views.privacy_policy),
]