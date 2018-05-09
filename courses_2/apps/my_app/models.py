# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course must be longer than 5 characters"
        return errors
class DescriptionManager(models.Manager):
    def second_validator(self, postData):
        errors = {}
        if len(postData['desc']) < 15:
            errors['desc'] = "Description must be longer than 15 characters"
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
class Description(models.Model):
    content = models.CharField(max_length=255)
    course = models.OneToOneField(Course, related_name="description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DescriptionManager()