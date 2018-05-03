# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 0
    return render(request, 'my_app/index.html')
def submit(request):
    request.session['counter'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')
def result(request):
    context = {
        "name": request.session['name'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comment": request.session['comment'],
        "counter": request.session['counter']
    }
    return render(request, 'my_app/result.html', context)
