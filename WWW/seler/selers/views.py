from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import datetime

from selers.models import Product, Seller, Client

# Create your views here.

def home_view(request):

    data = datetime.datetime.now()

    
    try:
        potd = data.day - (data.day // 2 + 2)
    
    except:
        potd = 1

    produkt = Product.objects.filter(id=potd)

    all_products = Product.objects.all()
    context = {
        'message': 'Witaj na stronie głównej',
        'products': all_products,
        'potd': produkt
    }

    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username = username, password = password)
           login(request, user)
           return redirect('home')
    else:
       form = UserCreationForm()
    return render(request,'register.html', {'form': form})

def help(request):
    return render(request, 'help.html')

def product_details(request):
    return render(request, 'product_details.html')

def categories(request):
    return render(request, 'categories.html')

def product_details(request, id):

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        product = None

    context = {
        'product': product
    }

    return render(request, 'product_details.html', context)

def profilePage(request):

    if not request.user.is_authenticated:

        return redirect('login')
    
    else:
        return render(request, 'profilePage.html')