from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Restaurants, Touristspot
import cloudinary.uploader

# Home View
def home(request):
    return render(request, 'home.html')

# User Login View
def login_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard') # Redirect to user dashboard
        return HttpResponse('Incorrect username or password', status=401)
    return render(request, 'login_user.html')

def user_dashboard(request):
    return render(request,'user_dashboard.html')



# User Signup View
def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return HttpResponse("Signup successful!")
    return render(request, 'signup.html')

# Admin Login View
def login_admin(request):
    if request.method=='POST':
        username=request.POST.get('admin_username')
        password=request.POST.get('admin_password')
        admin=authenticate(request,email=username,password=password)
        return redirect('admin_dashboard')
    return render(request,'login_admin.html')


def admin_dashboard (request):
    return rednder(request,'admin_dashboard.html')

# Add Restaurant View
@login_required
def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        image = request.FILES.get('image')
        result = cloudinary.uploader.upload(image)
        image_url = result.get('url')
        Restaurant.objects.create(name=name, address=address, image=image_url)
        return redirect('admin_dashboard')
    return render(request, 'add_restaurant.html')

# Edit Restaurant View
@login_required
def edit_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        restaurant.name = request.POST['name']
        restaurant.address = request.POST['address']
        if 'image' in request.FILES:
            result = cloudinary.uploader.upload(request.FILES['image'])
            restaurant.image = result.get('url')
        restaurant.save()
        return redirect('admin_dashboard')
    return render(request, 'edit_restaurant.html', {'restaurant': restaurant})

# Delete Restaurant View
@login_required
def delete_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    restaurant.delete()
    return redirect('admin_dashboard')

# Add Tourist Spot View
@login_required
def add_tourist_spot(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        image = request.FILES.get('image')
        result = cloudinary.uploader.upload(image)
        image_url = result.get('url')
        TouristSpot.objects.create(name=name, address=address, image=image_url)
        return redirect('admin_dashboard')
    return render(request, 'add_tourist_spot.html')

# Edit Tourist Spot View
@login_required
def edit_tourist_spot(request, id):
    tourist_spot = get_object_or_404(TouristSpot, id=id)
    if request.method == 'POST':
        tourist_spot.name = request.POST['name']
        tourist_spot.address = request.POST['address']
        if 'image' in request.FILES:
            result = cloudinary.uploader.upload(request.FILES['image'])
            tourist_spot.image = result.get('url')
        tourist_spot.save()
        return redirect('admin_dashboard')
    return render(request, 'edit_tourist_spot.html', {'tourist_spot': tourist_spot})

# Delete Tourist Spot View
@login_required
def delete_tourist_spot(request, id):
    tourist_spot = get_object_or_404(TouristSpot, id=id)
    tourist_spot.delete()
    return redirect('admin_dashboard')
