from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('ad_login/', views.ad_login, name="ad_login"),
    path('user_login/', views.user_login, name="user_login"),
]
