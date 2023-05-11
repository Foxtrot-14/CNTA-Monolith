from django.shortcuts import reverse
from django.db import models
from django.contrib.auth import get_user_model
from phone_field import PhoneField
from django.utils import timezone

User = get_user_model() 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)
    def __str__(self):
        return self.user.username
   
class Child(models.Model):
    boolChoice = [
        ("M","Male"),("F","Female")
        ]
    child_id = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=20,null=False,blank=False)
    lName =  models.CharField(max_length=20,null=False,blank=False)
    sex = models.CharField(max_length = 1,choices=boolChoice,null=False,blank=False)
    father = models.CharField(max_length=20,null=False,blank=False)
    fnumber = PhoneField(max_length=15,null=False,blank=False)
    mother = models.CharField(max_length=20,null=False,blank=False)
    mnumber = PhoneField(max_length=15,null=False,blank=False)
    age = models.FloatField(max_length=5,null=False,blank=False)
    weight = models.FloatField(max_length=5,null=False,blank=False)
    height = models.FloatField(max_length=5,null=False,blank=False)
    headcir = models.FloatField(max_length=5,null=False,blank=False)
    muac = models.FloatField(max_length=5,null=False,blank=False)
    chestCir = models.FloatField(max_length=5,null=False,blank=False)
    date = models.DateField(default=timezone.now)
    diagnosis = models.CharField(max_length=50, null=True,blank=True)
    referredto = models.CharField(max_length=50, null=True,blank=True)
    adder = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_pics')
    slug=models.SlugField()
    def __str__(self):
        return self.fName
    