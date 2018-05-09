# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')
def register(request):
    errors = User.objects.reg(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password)
        request.session['user'] = User.objects.get(email=request.POST['email']).id
        request.session['action']="registered"
        return redirect('/result')
def login(request):
    errors = User.objects.log(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['user'] = User.objects.get(email=request.POST['email']).id
        request.session['action'] = "logged in"
        return redirect('/result')
def result(request):
    context = {
        "hi": User.objects.get(id=request.session['user'])
    }
    return render(request, 'my_app/result.html', context)