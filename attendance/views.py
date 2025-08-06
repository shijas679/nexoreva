from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Attendance
from django.contrib.auth.decorators import login_required

@login_required
def attendance_home(request):
    return render(request, 'attendance/attendance.html')

@login_required
def records(request):
    records = Attendance.objects.filter(user=request.user)
    return render(request, 'attendance/records.html', {'records': records})

@login_required
def time_in(request):
    today = timezone.now().date()
    Attendance.objects.get_or_create(
        user=request.user,
        date=today,
        defaults={'time_in': timezone.now().time()}
    )
    return redirect('attendance_home')

@login_required
def time_out(request):
    today = timezone.now().date()
    try:
        att = Attendance.objects.get(user=request.user, date=today)
        att.time_out = timezone.now().time()
        att.save()
    except Attendance.DoesNotExist:
        pass
    return redirect('attendance_home')
