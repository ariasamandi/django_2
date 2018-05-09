# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'course': Course.objects.all(),
        "description": Description.objects.all()
    }
    return render(request, 'my_app/index.html', context)
def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(content=request.POST['desc'], course=course)
        return redirect('/')
def destroy_page(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    request.session['user_id'] = id
    return render(request, 'my_app/destroy.html', context)
def destroy(request):
    Course.objects.get(id = request.session['user_id']).delete()
    return redirect('/') 