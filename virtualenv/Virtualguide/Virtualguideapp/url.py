from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_users, name='login_users'),
    path('signup/', views.signup_user, name='signup_user'),
    path('logout/', views.logout, name='logout'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),  # User dashboard


    # Admin authentication
    path('login_admin', views.login_admin, name='admin_login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),

    # Restaurant CRUD
    path('admin/restaurant/add/', views.add_restaurant, name='add_restaurant'),
    path('admin/restaurant/edit/<int:id>/', views.edit_restaurant, name='edit_restaurant'),
    path('admin/restaurant/delete/<int:id>/', views.delete_restaurant, name='delete_restaurant'),

    # Tourist Spot CRUD
    path('admin/tourist/add/', views.add_tourist_spot, name='add_tourist_spot'),
    path('admin/tourist/edit/<int:id>/', views.edit_tourist_spot, name='edit_tourist_spot'),
    path('admin/tourist/delete/<int:id>/', views.delete_tourist_spot, name='delete_tourist_spot'),
]
