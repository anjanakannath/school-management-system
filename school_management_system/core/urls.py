from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('librarian_dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
]