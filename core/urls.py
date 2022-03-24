from django.urls import path
from django.http import JsonResponse
from .views import *
urlpatterns = [
    path('',get_user)
]