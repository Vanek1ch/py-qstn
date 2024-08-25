from django.db import models
from django import forms

# Create your models here.
class UserManager(models.Manager):
    def check_user_existing(self, login):
        if not login:
            raise ValueError("There is no login to search.")
        else:
            user = User.objects.filter(login=login).exists()

    def create_user(self, login, password, email, salt):
        if not email:
            raise ValueError("User must have an email.")
        if not login:
            raise ValueError("User must have a login.")
        if not password:
            raise ValueError("User must have a password.")
        else:
            if User.objects.filter(login=login).exists() or User.objects.filter(email=email).exists():
                raise Exception("User is already exists.")
            else:
                user = User(login=login, password=password,email=email, salt=salt)
                user.save()
        return user

class User(models.Model):
    login = models.CharField(max_length=32, unique=True)
    password = models.TextField()
    email = models.EmailField(max_length=100, unique=True)
    salt = models.TextField(default=1)
    created_on = models.DateField(auto_now_add=True)
    
    objects = UserManager()