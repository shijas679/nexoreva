from django.db import models
from django.contrib.auth.models import User
import random
from django.urls import reverse
from django.core.exceptions import ValidationError

def generate_unique_code(role_prefix):
    number = ''.join(random.choices('0123456789', k=4))
    return f"{role_prefix}{number}"

class Staff(models.Model):
    """
    Staff Model to hold employee/intern records.
    Includes personal, professional, and document-related details.
    """

    ROLE_CHOICES = [
        ('Employee', 'Employee'),
        ('Intern', 'Intern'),
    ]

    DEPARTMENT_CHOICES = [
        ('HR', 'HR'),
        ('Engineering', 'Engineering'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
        ('Operations', 'Operations'),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    ]

    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        ('Documents pending', 'Documents pending'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    designation = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    reporting_manager = models.CharField(max_length=100, blank=True, null=True)
    join_date = models.DateField()

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)

    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()

    id_proof = models.FileField(upload_to='id_proofs/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    offer_letter = models.FileField(upload_to='offer_letters/', null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    admin_notes = models.TextField(blank=True, null=True)

    staff_code = models.CharField(max_length=20, unique=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # New: Timestamp when record is created
    updated_at = models.DateTimeField(auto_now=True)      # New: Timestamp when record is updated

    def save(self, *args, **kwargs):
        # Generate unique staff code if not already set
        if not self.staff_code:
            prefix = 'nxrint' if self.role == 'Intern' else 'nxremp'
            while True:
                new_code = generate_unique_code(prefix)
                if not Staff.objects.filter(staff_code=new_code).exists():
                    self.staff_code = new_code
                    break

        # Optional: Run full validation before saving
        self.full_clean()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Optional: Used for redirects after saving
        return reverse('staff_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Staff Member'
        verbose_name_plural = 'Staff Members'
