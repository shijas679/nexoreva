from django.db import models
from django.contrib.auth.models import User
from staff.models import Staff

class Course(models.Model):
    COURSE_CHOICES = [
        ('IT', 'IT'),
        ('Engineering', 'Engineering'),
        ('Medical', 'Medical'),
    ]
    SUB_COURSE_CHOICES = [
        ('', '---------'), # Placeholder, will be set dynamically in forms
    ]
    name = models.CharField(max_length=255, choices=COURSE_CHOICES)
    sub_course = models.CharField(max_length=255, choices=SUB_COURSE_CHOICES, blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)  # Changed back to Staff
    enrolled_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('course', 'staff')  # Prevent duplicate enrollments

    def __str__(self):
        return f"{self.staff.full_name} enrolled in {self.course.name}"
