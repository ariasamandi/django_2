# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    my_id = get_random_string(length=14)
    context = {
        "word": request.session['generate'],
        "generate": my_id
    }
    return render(request, 'my_app/index.html', context)
def generate(request):
    request.session['generate'] += 1
    return redirect('/')
def reset(request):
    request.session['generate'] = 1
    return redirect('/')