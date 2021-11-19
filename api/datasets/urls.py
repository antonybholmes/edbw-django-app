from django.urls import path
from django.conf.urls import url

from api.datasets import views

urlpatterns = [
    path('', views.datasets, name='datasets'),
]
