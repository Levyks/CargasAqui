from django.urls import path

from . import views

urlpatterns = [
    path('auth/login/', views.showLogin, name='login'),
    path('cargas', views.listCargas, name='cargas'),
]