from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('check1/', views.check1, name='check1'),
    path('check2/', views.check2, name='check2'),
    path('company/', views.company, name='company'),
    path('fb/', views.feedback, name='fb'),
    path('qr/', views.qr, name='qr'),
    path('main/', views.main, name='main'),
    path('accept_list/', views.accept_list, name='accept_list'),

    path('', views.home, name="home"),
    path('detail/<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('update/<int:blog_id>/', views.update, name="update"),
    path('updateAction/<int:blog_id>/', views.updateAction, name="updateAction"),
    path('delete/<int:blog_id>/', views.delete, name="delete"),
]

