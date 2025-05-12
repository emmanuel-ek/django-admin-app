from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from ..forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout


def auth_register(request):
    return render(request, 'authentication/register.html')

def auth_store(request):
    form = RegistrationForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'authentication/register.html', {'form': form})
    
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    user.save()
    return redirect('login')

def auth_login(request):
    return render(request, 'authentication/login.html')

def auth_handle_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'authentication/login.html')

def auth_handle_logout(request):
    logout(request)
    return redirect('login_view') 