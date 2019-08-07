from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new),
    path('create/', views.create),
    # Read
    path('', views.index),
]
