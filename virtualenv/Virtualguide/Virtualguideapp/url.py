from django.urls import path
from Virtualguideapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login_users',views.login_users,name='login_users'),
    path('signup_user',views.signup_user,name='signup_user')
]