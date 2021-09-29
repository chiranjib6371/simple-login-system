from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signin(request):

    if request.method == "POST":
        email = request.POST['email']
        pass1 = request.POST['pass1']

        user = authenticate(email=email,password=pass1)

        if user is not None:
            login(request, user)
            name = user.name
            return render(request, "authentication/index.html",{'name': name} )
        else:
            messages.error(request, "bad credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username)
        myuser.username = username
        myuser.name = name
        myuser.email = email
        myuser.address = address
        myuser.pass1 = pass1
        myuser.pass2 = pass2
    
        myuser.save()
        messages.success(request, "Your account has been successfully created")

        return redirect('signin')
    
    return render(request, "authentication/signup.html")

def Logout(request):
    logout(request)
    message.success(request, "Logged Out Successfully!")
    return redirect('home')
    pass        
