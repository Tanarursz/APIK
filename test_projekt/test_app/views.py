from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'test_app/index.html')

def rolam(request):
    return render(request, 'test_app/rolam.html')

def kapcsolat(request):
    return render(request, 'test_app/kapcsolat.html')

