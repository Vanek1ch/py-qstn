from django.contrib.auth.backends import BaseBackend
from .models import UserManager

class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
