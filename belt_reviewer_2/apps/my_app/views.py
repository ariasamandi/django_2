# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')
def reg(request):
    hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['user'] = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=hash1)
        return redirect('/books')
def log(request):
    errors = User.objects.log_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['user'] = User.objects.get(email = request.POST['email']).id
    return redirect('/books')
def books(request):
    context = {
        "user": User.objects.get(id=request.session['user'])
    }
    return render(request, 'my_app/books.html', context)