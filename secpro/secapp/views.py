from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mesh(request):
    return HttpResponse("helo")
def index(request):
    return render(request,"index.html")
def index2(request):
    return render(request,"index2.html")
def index3(request):
    return render(request,"index3.html")
def index4(request):
    return render(request,"index4.html")
