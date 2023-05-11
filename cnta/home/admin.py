from django.contrib import admin
from django.contrib.auth.models import User
from . models import Profile,Child
# Register your models here.
admin.site.register(Profile)
admin.site.register(Child)