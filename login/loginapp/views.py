from django.shortcuts import render
from . models import Gallery

# Create your views here.
def signin(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'index2.html')

