from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('librarian_dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
]