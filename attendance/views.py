from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.timezone import localtime
from django.contrib import messages
from .models import Attendance, LeaveRequest
from staff.models import Staff
from .forms import StaffCodeForm, LeaveRequestForm
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta, datetime
from django.db.models import Q
from .models import Daily_Task


def attendance_home(request):
    return render(request, 'attendance/attendance_home.html')


def attendance_action(request):
    if request.method == 'POST':
        staff_code = request.POST.get('staff_code')
        action = request.POST.get('action')
        staff = Staff.objects.filter(staff_code=staff_code).first()

        if not staff:
            messages.error(request, "Invalid staff code.")
            return redirect('attendance_home')

        today = timezone.localdate()
        att, _ = Attendance.objects.get_or_create(staff=staff, date=today)

        now = localtime(timezone.now()).time()

        if action == 'time_in':
            if att.time_in:
                messages.info(request, f"{staff.full_name} already timed in today.")
            else:
                att.time_in = now
                att.save()
                messages.success(request, f"{staff.full_name} timed in successfully!")
        elif action == 'time_out':
            if not att.time_in:
                messages.error(request, f"{staff.full_name} has not timed in today.")
            elif att.time_out:
                messages.info(request, f"{staff.full_name} already timed out today.")
            else:
                att.time_out = now
                att.save()
                messages.success(request, f"{staff.full_name} timed out successfully!")
        else:
            messages.error(request, "Please select Time In or Time Out.")

        return redirect('attendance_home')
    else:
        return redirect('attendance_home')


def leave_request(request):
    form = LeaveRequestForm(request.POST or None)

    if request.method == 'POST':
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
                messages.success(request, f"Leave request submitted successfully for {staff.full_name}.")
                return redirect('attendance_home')
            else:
                messages.error(request, "Invalid Staff Code. Please try again.")
        else:
            messages.error(request, "There was an error in the form. Please check the details.")

    return render(request, 'attendance/leave_request.html', {'form': form})


def attendance_details(request):
    today = date.today()
    search_query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', '')

    from_date_str = request.GET.get('from_date')
    to_date_str = request.GET.get('to_date')

    def parse_date(val, fallback):
        try:
            return datetime.strptime(val, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            return fallback

    from_date = parse_date(from_date_str, today)
    to_date = parse_date(to_date_str, today)

    if from_date > to_date:
        from_date, to_date = to_date, from_date

    all_staff = Staff.objects.all()
    if search_query:
        all_staff = all_staff.filter(Q(full_name__icontains=search_query))

    attendance_details = []
    delta_days = (to_date - from_date).days + 1
     
    for staff in all_staff:
        for offset in range(delta_days):
            current_date = from_date + timedelta(days=offset)

            attendance = Attendance.objects.filter(staff=staff, date=current_date).first()
            on_leave = LeaveRequest.objects.filter(
                staff=staff, from_date__lte=current_date, to_date__gte=current_date
            ).exists()

            if attendance:
                status = "Present"
                time_in = attendance.time_in
                time_out = attendance.time_out
            elif on_leave:
                status = "On Leave"
                time_in = time_out = None
            else:
                status = "Absent"
                time_in = time_out = None

            status_class = status.lower().replace(' ', '-')

            if status_filter and status != status_filter:
                continue

            attendance_details.append({
                'staff': staff,
                'date': current_date,
                'time_in': time_in,
                'time_out': time_out,
                'status': status,
                'status_class': status_class,
            })

    attendance_details.sort(key=lambda d: (d['date'], d['staff'].full_name))

    return render(request, 'attendance/attendence_list.html', {
        'attendance_details': attendance_details,
        'search_query': search_query,
        'status_filter': status_filter,
        'from_date': from_date.strftime("%Y-%m-%d"),
        'to_date': to_date.strftime("%Y-%m-%d"),
    })


def leave_details(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    query = request.GET.get('q', '')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    records = LeaveRequest.objects.filter(staff=staff).order_by('-request_date')

    if query:
        records = records.filter(Q(reason__icontains=query))
    if from_date:
        records = records.filter(from_date__gte=from_date)
    if to_date:
        records = records.filter(to_date__lte=to_date)

    context = {
        'staff': staff,
        'records': records,
        'query': query,
        'from_date': from_date,
        'to_date': to_date,
    }
    return render(request, 'attendance/leave_details.html', context)


def add_task(request):
    error_message = None
    if request.POST:
        staff_code = request.POST['staff_code']
        task = request.POST['task']
        try:
            staff_obj = Staff.objects.get(staff_code=staff_code)
            daily_task_obj = Daily_Task.objects.create(staff_code=staff_code, task=task)
            daily_task_obj.save()
        except:
            error_message = "Staff doesn't Exist"
    return render(request, 'attendance/add_task.html', {'error_message': error_message})
