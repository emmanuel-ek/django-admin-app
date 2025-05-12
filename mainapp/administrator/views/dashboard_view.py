from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


@require_GET
@login_required(login_url='login_view')
def get_dashboard(request):
    return render(request, 'dashboard/index.html')