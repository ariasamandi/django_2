# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def reg(self, postData):
        errors = {}
        if len(postData['first_name']) < 5:
            errors['first_name'] = "First name is too short"
        if len(postData['last_name']) < 5:
            errors['last_name'] = "Last name is too short"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is invalid"
        if len(postData['password']) < 5:
            errors['password'] = "password is too short"
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['jeffispoop'] = "email is taken"
        return errors
    def log(self, postData):
        errors = {}
        try:
            user=User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['message'] = "Emal or password is invalid"
        except User.DoesNotExist:
            errors['message'] = "Email or password is invalid"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()