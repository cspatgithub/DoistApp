from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    # authentication
    path('signup/', views.SignUpView, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # profile
    path('<slug:slug>', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('<slug:slug>/update', views.ProfileUpdateView.as_view(), name='profile-update')
]