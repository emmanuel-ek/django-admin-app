from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import dashboard_view, auth_view, category_view, profile_view


urlpatterns = [
    # Dashboard
    path('dashboard/', dashboard_view.get_dashboard, name='dashboard'),
    
    # Authentication
    path('register/', auth_view.auth_register, name='register'),
    path('register/store/', auth_view.auth_store, name='register_store'),
    path('login/', auth_view.auth_handle_login, name='login'),
    path('login/view', auth_view.auth_login, name='login_view'),
    path('logout/', auth_view.auth_handle_logout, name='logout'),
    
    # Category
    path('categories/', category_view.get_categories, name='category_list'),
    path('categories/create/', category_view.create_category, name='category_create'),
    path('categories/store/', category_view.store_category, name='category_store'),
    path('category/<int:id>/delete/', category_view.delete_category, name='delete_category'),
    
    # Profile
    path('profile/<int:id>/edit/', profile_view.edit_profile, name='edit_profile'),
    path('profile/update/', profile_view.update_profile, name='update_profile')
]