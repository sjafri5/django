from django.shortcuts import render
from time import gmtime, strftime

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    count = request.session.get('count', 0)
    word = get_random_string(length=32)
    # request.session['count'] = count

    print('xxxxxxxxxxxxxxxxxxxxxxx', request.session.get('count'))
    context = {
        "count": count,
        "word": word
    }

    return render(request, "random_word/index.html", context)

def create(request):
    request.session['count'] = request.session.get('count') + 1
    return redirect("/")
