from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    x = 1 + 19
    return render(request, 'home.html',{'name': 'Hedeiwy', 'age': x}) # this is what the home function will return to the urls