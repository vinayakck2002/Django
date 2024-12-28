from django.shortcuts import render,redirect
from . models import Gallery
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # Check if both fields are provided
        if not username or not password:
            messages.error(request, "Both username and password are required!")
            return render(request, 'index.html')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(index)  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'index.html')

def index(request):
    return render(request,'index3.html')

def usersignup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        print(email,username,password,confirmpassword)
        if password==confirmpassword:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect("signin")
        
       
        
    
    return render(request, "index2.html")