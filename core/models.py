from typing import AbstractSet
from django.db import models 
from django.contrib.auth.models import User

userType=(
    (0,'Admin'),
    (1,'Cliente'),
    (2,'Profesional')
         )

class userModel(models.Model):
    userRut= models.CharField(max_length=30 , unique= True)
    userType= models.IntegerField(choices=userType)

    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="extend")

    def __str__(self):
        return self.userRut


