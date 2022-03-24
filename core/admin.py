from django.contrib import admin

from .models import Kids,Food
# Register your models here.
admin.site.register(Kids)

class FoodAdmin(admin.ModelAdmin):
    class Media:
        js=('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js','js/admin.js')

admin.site.register(Food,FoodAdmin)