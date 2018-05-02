# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.
def index(request):
    context = {
        "time": strftime("%B %d, %Y %I:%M %p", gmtime())
    }
    return render(request, 'my_app/index.html', context)