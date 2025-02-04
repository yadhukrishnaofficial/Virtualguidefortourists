from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def home(request):
    return render(request,'home.html')

def login_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        username = user.username
        users = authenticate(request, username=username, password=password)
        if users is not None:
            login(request, users)
            return HttpResponse("Login Succesfull")
        else:
            return HttpResponse('Incorrect username or password')
    return render(request, 'login_user.html')

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return HttpResponse({"message": "Signup successful!"})
    return render(request, "signup.html")