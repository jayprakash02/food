from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('utils/',include('core.urls')),
    path('', admin.site.urls),
]