from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from ..forms import UserForm


@require_GET
@login_required(login_url='login_view')
def edit_profile(request, id):
    user = User.objects.get(is_superuser=1)
    return render(request, 'profile/edit.html', {'user': user, 'user_id': id})


@require_POST
@login_required(login_url='login_view')
def update_profile(request):
    form = UserForm(request.POST, instance=request.user)
    if not form.is_valid():
        return render(request, 'profile/edit.html', {'form': form})
    
    form.save()
    return redirect('edit_profile', id=request.user.id)