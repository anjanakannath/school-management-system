from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    enrollment_number = models.CharField(max_length=20, unique=True)
    class_level = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LibraryRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='library_records')
    book_title = models.CharField(max_length=200)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book_title} - {self.student.first_name}"

class FeesRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees_records')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.student.first_name} - {self.amount_paid}"
