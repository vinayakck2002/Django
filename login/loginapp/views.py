from django.shortcuts import render
from . models import Gallery

# Create your views here.
def viewsmain(request):
    return render(request,'index.html')

