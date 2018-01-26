from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    context = {"user":["number", "alpha", "dec", "hex", "oct", "roman"]}
    return render(request, 'store/index.html', context)