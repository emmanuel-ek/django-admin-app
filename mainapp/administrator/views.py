from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout



@require_GET
def get_dashboard(request):
    return render(request, 'dashboard/index.html')

@require_GET
def get_categories(request):
    categories = Category.objects.all()
    data = list(categories.values()) if categories else []
    return render(request, 'category/index.html', {'categories': data})

@require_GET
def create_category(request):
    return render(request, 'category/create.html')


@require_POST
def store_category(request):
    form = CategoryForm(request.POST)
    if not form.is_valid():
        return render(request, 'category/create.html', {'form': form})
    
    form.save()
    return redirect('category_list')

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_list')

# authentication routes
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
    
