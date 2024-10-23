from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Office Staff'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def is_admin(self):
        return self.role == 'admin'

    def is_staff(self):
        return self.role == 'staff'

    def is_librarian(self):
        return self.role == 'librarian'
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=50)
    roll_number = models.IntegerField(unique=True)

class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    return_date = models.DateField()

class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField()

