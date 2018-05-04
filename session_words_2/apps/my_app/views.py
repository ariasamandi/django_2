# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import strftime
# Create your views here.
def index(request):
    if not 'words' in request.session:
        request.session['words'] = []
    return render(request, 'my_app/index.html')
def process(request):
    if not 'color' in request.POST:
        color = 'black'
    else:
        color = request.POST['color']
    if not 'big' in request.POST:
        big = 0
    else:
        big = request.POST['big']
    words = {
        "words": request.session['input'],
        "color": color,
        'time': str(strftime("%H:%M:%S, %B, %m %Y")),
        'big': big
    }
    request.session['words'].append(words)
    request.session.modified = True
    return redirect('/')
def process2(request):
    request.session['words']=[]
    return redirect('/')