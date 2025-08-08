# course/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from staff.models import Staff
from .models import Course, Enrollment
from .forms import CourseForm

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

def delete_courses(request):
    if request.method == 'POST':
        course_ids = request.POST.getlist('course_ids')
        
        if not course_ids:
            messages.error(request, 'No courses selected for deletion.')
            return redirect('course_list')
        
        try:
            # Delete the selected courses
            deleted_count = Course.objects.filter(id__in=course_ids).delete()[0]
            
            if deleted_count == 1:
                messages.success(request, f'{deleted_count} course has been deleted successfully.')
            else:
                messages.success(request, f'{deleted_count} courses have been deleted successfully.')
                
        except Exception as e:
            messages.error(request, f'Error deleting courses: {str(e)}')
    
    return redirect('course_list')
