from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [

    path('', views.login_view, name='login'),   
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),

    path('students/', views.view_students, name='view_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),

    path('library/', views.library_history, name='library_history'),
    path('library/add/', views.add_library_record, name='add_library_record'),
    path('library/edit/<int:record_id>/', views.edit_library_record, name='edit_library_record'),
    path('library/delete/<int:record_id>/', views.delete_library_record, name='delete_library_record'),

    path('fees/', views.fees_history, name='fees_history'),
    path('fees/add/', views.add_fees_record, name='add_fees_record'),
    path('fees/edit/<int:record_id>/', views.edit_fees_record, name='edit_fees_record'),
    path('fees/delete/<int:record_id>/', views.delete_fees_record, name='delete_fees_record'),
]
