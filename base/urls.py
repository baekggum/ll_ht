from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_base, name="new_base"),
]

