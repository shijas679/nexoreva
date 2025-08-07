# course/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from staff.models import Staff
from .models import Course, Enrollment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'start_date', 'end_date', 'payment_amount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter course description'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter payment amount'}),
        }

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    
    return render(request, 'course/add_course.html', {'form': form})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    return render(request, 'course/course_detail.html', {
        'course': course,
        'enrollments': enrollments
    })

def enroll_user(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        staff_code = request.POST.get('staff_code')
        try:
            staff = Staff.objects.get(staff_code=staff_code)
        except Staff.DoesNotExist:
            return render(request, 'course/enroll_user.html', {
                'course': course,
                'error': 'No staff member found with this unicode.'
            })

        if Enrollment.objects.filter(course=course, staff=staff).exists():
            return render(request, 'course/enroll_user.html', {
                'course': course,
                'error': 'This staff member is already enrolled.'
            })

        Enrollment.objects.create(course=course, staff=staff)
        return redirect('course_detail', course_id=course.id)

    return render(request, 'course/enroll_user.html', {'course': course})

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/edit_course.html', {'form': form, 'course': course})
