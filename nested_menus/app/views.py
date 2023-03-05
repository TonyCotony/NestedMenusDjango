from django.http import HttpResponseNotFound
from django.shortcuts import render


def show_menu(request, name):
    return render(request, 'app/index.html', {'name': name})


def about(request):
    return render(request, 'app/about.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>This page not found, try another urls<h1/>')
