import imp
from pickle import FALSE
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
# Create your views here.
def get_user(request):
    
    return JsonResponse({'user':request.user.id},safe=False)