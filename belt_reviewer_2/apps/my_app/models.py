# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name need to be longer than 2 characters"
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias need to be longer than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is invalid"
        if len(postData['password']) < 4:
            errors['password'] = "password need to be longer than 4 characters"
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password and confirm password dont match"
        if User.objects.filter(email=postData['email']):
            errors['exist'] = "email already exists"
        return errors
    def log_validator(self, postData):
        errors = {}
        try:
            if User.objects.get(email = postData['email']):
                if not bcrypt.checkpw(postData['password'].encode(), User.objects.get(email = postData['email']).password.encode()):
                    errors['bcrypt'] = "Email or password is invalid"
                else:
                    return errors
        except:
            errors['no_user'] = "Email or password is invalid"
        return errors
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Review(models.Model):
    content = models.CharField(max_length=255)
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)