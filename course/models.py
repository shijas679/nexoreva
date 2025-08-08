from django.db import models
from django.contrib.auth.models import User
from staff.models import Staff
import random

class Course(models.Model):
    COURSE_CHOICES = [
        ('IT', 'IT'),
        ('Engineering', 'Engineering'),
        ('Medical', 'Medical'),
    ]

    SUB_COLUMN_CHOICES = [
        ('', '---------'),
        ('Web Development', 'Web Development'),
        ('Data Science', 'Data Science'),
        ('Networking', 'Networking'),
        ('Cyber Security', 'Cyber Security'),
        ('Computer Science Engineering (CSE)', 'Computer Science Engineering (CSE)'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('MBBS (Bachelor of Medicine & Bachelor of Surgery)', 'MBBS (Bachelor of Medicine & Bachelor of Surgery)'),
        ('BDS (Bachelor of Dental Surgery)', 'BDS (Bachelor of Dental Surgery)'),
        ('BAMS (Ayurveda)', 'BAMS (Ayurveda)'),
        ('BHMS (Homeopathy)', 'BHMS (Homeopathy)'),
    ]

    name = models.CharField(max_length=255, choices=COURSE_CHOICES)
    sub_column = models.CharField(max_length=255, choices=SUB_COLUMN_CHOICES, blank=True)
    unicode = models.CharField(max_length=10, unique=True, blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if not self.unicode:
            self.unicode = self.generate_unicode()
        super().save(*args, **kwargs)

    def generate_unicode(self):
        # Generate prefix based on course name
        if self.name == 'IT':
            prefix = 'IT'
        elif self.name == 'Engineering':
            prefix = 'ENG'
        elif self.name == 'Medical':
            prefix = 'MED'
        else:
            prefix = 'GEN'
        
        # Generate 5 random digits
        digits = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        
        return f"{prefix}{digits}"

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