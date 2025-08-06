from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Course, Enrollment
from django.contrib.auth.models import User


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        Course.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('course_list')

    return render(request, 'course/add_course.html')

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollments = Enrollment.objects.filter(course=course).select_related('user')
    return render(request, 'course/course_detail.html', {
        'course': course,
        'enrollments': enrollments
    })

def enroll_user(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        unicode = request.POST['unicode']
        try:
            user = User.objects.get(userprofile__unicode=unicode)
        except User.DoesNotExist:
            return render(request, 'course/enroll_user.html', {
                'course': course,
                'error': 'No user found with this unicode.'
            })

        # Prevent duplicate
        if Enrollment.objects.filter(course=course, user=user).exists():
            return render(request, 'course/enroll_user.html', {
                'course': course,
                'error': 'User already enrolled in this course.'
            })

        Enrollment.objects.create(course=course, user=user)
        return redirect('course_detail', course_id=course.id)

    return render(request, 'course/enroll_user.html', {'course': course})
