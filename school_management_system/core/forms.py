from django import forms
from .models import Student, LibraryRecord, FeesRecord

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'enrollment_number', 'class_level', 'address', 'email', 'phone_number']

class LibraryRecordForm(forms.ModelForm):
    class Meta:
        model = LibraryRecord
        fields = ['student', 'book_title', 'issue_date', 'return_date']

class FeesRecordForm(forms.ModelForm):
    class Meta:
        model = FeesRecord
        fields = ['student', 'amount_paid', 'payment_date']
