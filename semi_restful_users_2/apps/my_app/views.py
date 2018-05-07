# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from models import *
# Create your views here.
def index(request):
    context = {
        "user" : User.objects.all()
    }
    return render(request, 'my_app/index.html', context)
def new(request):
    return render(request, 'my_app/new.html')
def edit(request, id):
    context = {
        "user" : User.objects.get(id=id)
    }
    request.session['user_id'] = id
    return render(request, 'my_app/edit.html', context)
def show(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, 'my_app/show.html', context)
def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/users')
def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')
def update(request):
    user = User.objects.get(id=request.session['user_id'])
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/{}/edit'.format(request.session['user_id']))
    else:
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users')