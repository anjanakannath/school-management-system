from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, LibraryRecord, FeesRecord
from .forms import StudentForm, LibraryRecordForm, FeesRecordForm

# Dashboard views
def dashboard(request):
    return render(request, 'dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html')

# Student views
def view_students(request):
    students = Student.objects.all()
    return render(request, 'students/view_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('view_students')
    return render(request, 'students/delete_student.html', {'student': student})

# Library views
def library_history(request):
    records = LibraryRecord.objects.all()
    return render(request, 'library/library_history.html', {'records': records})

def add_library_record(request):
    if request.method == 'POST':
        form = LibraryRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_history')
    else:
        form = LibraryRecordForm()
    return render(request, 'library/add_library_record.html', {'form': form})

def edit_library_record(request, record_id):
    record = get_object_or_404(LibraryRecord, id=record_id)
    if request.method == 'POST':
        form = LibraryRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('library_history')
    else:
        form = LibraryRecordForm(instance=record)
    return render(request, 'library/edit_library_record.html', {'form': form})

def delete_library_record(request, record_id):
    record = get_object_or_404(LibraryRecord, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('library_history')
    return render(request, 'library/delete_library_record.html', {'record': record})

# Fees views
def fees_history(request):
    records = FeesRecord.objects.all()
    return render(request, 'fees/fees_history_list.html', {'records': records})

def add_fees_record(request):
    if request.method == 'POST':
        form = FeesRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fees_history')
    else:
        form = FeesRecordForm()
    return render(request, 'fees/add_fees_record.html', {'form': form})

def edit_fees_record(request, record_id):
    record = get_object_or_404(FeesRecord, id=record_id)
    if request.method == 'POST':
        form = FeesRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('fees_history')
    else:
        form = FeesRecordForm(instance=record)
    return render(request, 'fees/edit_fees_record.html', {'form': form})

def delete_fees_record(request, record_id):
    record = get_object_or_404(FeesRecord, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('fees_history')
    return render(request, 'fees/delete_fees_record.html', {'record': record})
