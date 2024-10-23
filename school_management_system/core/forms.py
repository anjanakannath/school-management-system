from django import forms
from .models import Student, LibraryHistory, FeesHistory

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'class_name', 'roll_number']

class LibraryHistoryForm(forms.ModelForm):
    class Meta:
        model = LibraryHistory
        fields = ['student', 'borrowed_date', 'return_date']

class FeesHistoryForm(forms.ModelForm):
    class Meta:
        model = FeesHistory
        fields = ['student', 'amount', 'payment_date', 'remarks']
