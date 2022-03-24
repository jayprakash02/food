import re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_html_mail

# Create your models here.
class Kids(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    parent_phone=models.IntegerField()
    parent_email=models.EmailField()

    def __str__(self) -> str:
        return self.name

FOOD=(('Veg','Veg'),('Unknown','Unknown'))
class Food(models.Model):
    kid=models.ForeignKey(Kids,on_delete=models.CASCADE)
    image=models.URLField()
    group=models.CharField(max_length=20,choices=FOOD)
    created_on=models.DateTimeField(auto_now=True)
    updated_on=models.DateTimeField()
    isApproved=models.BooleanField()
    approved_by=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.kid.name

@receiver(post_save, sender=Food, dispatch_uid="new_food_added")
def new_food_added(sender, instance,created, **kwargs):
    if created:
        if(instance.group=='Unknown'):
           send_html_mail('Your Child eated unkown food','Hello Dear Parents here we want to inform you that your child has eated a unkown food!!',[instance.kid.parent_email])
        instance.save()