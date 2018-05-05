# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime
# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['log'] = []
        print request.session['log']
    return render(request, 'my_app/index.html')
def process(request, loc):
    if request.method != "POST":
        return redirect('/')
    if loc == 'farm':
        gold = random.randint(10, 21)
        log_str =  ("gain", "Earned {} gold from the {} ({})".format(gold, loc, datetime.datetime.now()))
    if loc == 'cave':
        gold = random.randint(5, 11)
        log_str = ("gain", "Earned {} gold from the {} ({})".format(gold, loc, datetime.datetime.now()))
    if loc == 'house':
        gold = random.randint(2, 6)
        log_str =  ("gain", "Earned {} gold from the {} ({})".format(gold, loc, datetime.datetime.now()))
    if loc == 'casino':
        gold = random.randint(-50, 51)
        if gold < 0:
            log_str = ("loss", "Lost {} gold from the {} ({})".format(abs(gold), loc, datetime.datetime.now()))
            color = "red"
        else:
            log_str = ("gain", "Earned {} gold from the {} ({})".format(gold, loc, datetime.datetime.now()))
            
    print log_str
    print loc
    print gold
    request.session['log'].insert(0, (log_str))
    print request.session['log']
    request.session['gold'] += gold
    return redirect('/')
def reset(request):
    request.session.clear()
    return redirect('/')