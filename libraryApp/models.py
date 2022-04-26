from django.db import models


# Create your models here.

class books(models.Model):
    title = models.CharField(max_length=100,null=False,unique=True)
    created_on = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30,null=False)
    availability = models.CharField(max_length=100,null=False,default="Yes")

class admin_users(models.Model):
    user_name = models.EmailField(unique=True)
    password = models.CharField(max_length=120,null=False)




    
    