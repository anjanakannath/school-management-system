from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, LibraryHistory, FeesHistory
from .forms import StudentForm, LibraryHistoryForm, FeesHistoryForm

from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

@login_required
def dashboard(request):
    if request.user.is_admin():
        return redirect('admin_dashboard')
    elif request.user.is_staff():
        return redirect('staff_dashboard')
    elif request.user.is_librarian():
        return redirect('librarian_dashboard')
    else:
        return redirect('login')

@login_required
def admin_dashboard(request):
    if not request.user.is_admin():
        return redirect('dashboard')
    # Admin-only functionality here
    return render(request, 'core/admin_dashboard.html')

@login_required
def staff_dashboard(request):
    if not request.user.is_staff():
        return redirect('dashboard')
    # Office Staff functionality here
    return render(request, 'core/staff_dashboard.html')

@login_required
def librarian_dashboard(request):
    if not request.user.is_librarian():
        return redirect('dashboard')
    # Librarian functionality here
    return render(request, 'core/librarian_dashboard.html')

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/add_student.html', {'form': form})

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/edit_student.html', {'form': form})

@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/confirm_delete.html', {'object': student})

