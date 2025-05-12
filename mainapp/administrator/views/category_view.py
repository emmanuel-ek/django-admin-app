from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Category
from ..forms import CategoryForm
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

@require_GET
@login_required(login_url='login_view')
def get_categories(request):
    categories = Category.objects.all()
    data = list(categories.values()) if categories else []
    return render(request, 'category/index.html', {'categories': data})

@require_GET
@login_required(login_url='login_view')
def create_category(request):
    return render(request, 'category/create.html')


@require_POST
@login_required(login_url='login_view')
def store_category(request):
    form = CategoryForm(request.POST)
    if not form.is_valid():
        return render(request, 'category/create.html', {'form': form})
    
    form.save()
    return redirect('category_list')

@login_required(login_url='login_view')
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_list')
