from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, MyKneegaaaa! 🎉 This is my first python django page.")

