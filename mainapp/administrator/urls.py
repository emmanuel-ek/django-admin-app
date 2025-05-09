from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

#app_name = 'admin'

urlpatterns = [
    # category
    path('dashboard', views.get_dashboard, name='dashboard'),
    path('categories/', views.get_categories, name='category_list'),
    path('categories/create/', views.create_category, name='category_create'),
    path('categories/store/', views.store_category, name='category_store'),
    path('category/<int:id>/delete', views.delete_category, name='delete_category'),
    
    #auth
    path('register/', views.auth_register, name='register'),
    path('register/store', views.auth_store, name='register_store'),
    path('login/', views.auth_handle_login, name='login'),
    path('login/view', views.auth_login, name='login_view'),
    path('logout/', views.auth_handle_logout, name='logout'),
]