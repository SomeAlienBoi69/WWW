from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

def home_view(request):
    context = {
        'message': 'Witaj na stronie głównej'
    }

    return render(request, 'home.html', context=context)

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