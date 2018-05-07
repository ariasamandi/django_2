# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'price' in request.session:
        request.session['price'] = 0
    if not 'total' in request.session:
        request.session['total'] = 0
    if not 'item' in request.session:
        request.session['item'] = 0
    return render(request, 'my_app/index.html')
def process(request, item):
    quantity = request.POST['quantity']
    if item == 'tshirt':
        price = 19.99
        total = price * int(quantity)
    elif item == 'sweater':
        price = 29.99
        total = price * int(quantity)
    elif item == 'cup':
        price = 4.99
        total = price * int(quantity)
    elif item == 'book':
        price = 49.99
        total = price * int(quantity)
    request.session['price'] = price
    request.session['total'] += total
    request.session['item'] += int(quantity)
    return redirect('/checkout')
def checkout(request):
    return render(request, 'my_app/checkout.html')
def reset(request):
    request.session.clear()
    return redirect('/')