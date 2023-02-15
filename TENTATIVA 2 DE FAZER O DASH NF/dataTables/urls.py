from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataTables, name="dataTables"),
]