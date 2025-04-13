
from django.shortcuts import render, redirect
from .models import MenuItem,Reservation
from .forms import ReservationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Reservation




def base(request):
    return render(request,'base.html')

def home(request):
    return render(request, 'home.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})

def contact(request):
    return render(request, 'contact.html')

def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'reserve.html',{'form':form})

def login_page(request):
   if request.method=="POST":
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request, user)
           return redirect('profile')
       else:
           messages.error(request,"Invalid username or password")
   return render(request,'login_page.html')

def manual_logout(request):
    logout(request)
    return redirect ('login_page')


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login_page')

    return render(request, 'signup.html')

@login_required(login_url='login_page')
def profile(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'profile.html', {'reservations':reservations})

