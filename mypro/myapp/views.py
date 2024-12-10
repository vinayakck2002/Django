from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def master(request):
    l=["mango\n","apple\n","grapes\n"]
    return HttpResponse(l)
