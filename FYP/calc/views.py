from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    x = 1 + 19
    # this is what the home function will return to the urls
    return render(request, 'home.html', {'name': 'Hedeiwy', 'age': x})


def add(request):

    a = int(request.GET['num'])
    b= int(request.GET['num2'])
    res= a + b

    return render(request, 'result.html', {'addition': res})
