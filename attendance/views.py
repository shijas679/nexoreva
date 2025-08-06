from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Attendance, LeaveRequest
from staff.models import Staff
from .forms import StaffCodeForm, LeaveRequestForm
from django.contrib.auth.decorators import login_required


def attendance_home(request):
    return render(request, 'attendance/attendance_home.html')

def attendance_action(request):
    if request.method == 'POST':
        staff_code = request.POST.get('staff_code')
        action = request.POST.get('action')  # 'time_in' or 'time_out'
        staff = Staff.objects.filter(staff_code=staff_code).first()
        if not staff:
            messages.error(request, "Invalid staff code.")
            return redirect('attendance_home')
        today = timezone.now().date()
        att, _ = Attendance.objects.get_or_create(staff=staff, date=today)
        if action == 'time_in':
            if att.time_in:
                messages.info(request, f"{staff.full_name} already timed in today.")
            else:
                att.time_in = timezone.now().time()
                att.save()
                messages.success(request, f"{staff.full_name} timed in successfully!")
        elif action == 'time_out':
            if not att.time_in:
                messages.error(request, f"{staff.full_name} has not timed in today.")
            elif att.time_out:
                messages.info(request, f"{staff.full_name} already timed out today.")
            else:
                att.time_out = timezone.now().time()
                att.save()
                messages.success(request, f"{staff.full_name} timed out successfully!")
        else:
            messages.error(request, "Please select Time In or Time Out.")
        return redirect('attendance_home')
    else:
        return redirect('attendance_home')


def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            staff_code = form.cleaned_data['staff_code']
            staff = Staff.objects.filter(staff_code=staff_code).first()
            if staff:
                LeaveRequest.objects.create(
                    staff=staff,
                    from_date=form.cleaned_data['from_date'],
                    to_date=form.cleaned_data['to_date'],
                    reason=form.cleaned_data['reason']
                )
                messages.success(request, f"Leave request submitted for {staff.full_name}.")
                return redirect('attendance_home')
            else:
                messages.error(request, "Invalid staff code.")
    else:
        form = LeaveRequestForm()
    return render(request, 'attendance/leave_request.html', {'form': form})
