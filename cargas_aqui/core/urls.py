from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/cargas')),
    path('cargas', views.listCargoes, name='cargas'),
]