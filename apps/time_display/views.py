from django.shortcuts import render
from time import gmtime, strftime

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }

    return render(request, "time_display/index.html", context)
