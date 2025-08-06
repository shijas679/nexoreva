from django.shortcuts import render, redirect
from .forms import StaffForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Staff member added successfully.")
            return redirect('add_staff')  
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = StaffForm()

    return render(request, 'staff/add_staff.html', {'form': form})

from django.shortcuts import render
from .models import Staff
from django.contrib.auth.decorators import login_required

@login_required
def view_staff(request):
    staff_list = Staff.objects.all().order_by('-id')  # Latest first
    return render(request, 'staff/view_staff.html', {'staff_list': staff_list})

from django.shortcuts import get_object_or_404

@login_required
def edit_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff details updated successfully.")
            return redirect('view_staff')
        else:
            messages.error(request, "Please correct the errors.")
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff/edit_staff.html', {'form': form, 'staff': staff})

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    staff.delete()
    messages.success(request, "🗑️ Staff member deleted successfully.")
    return redirect('view_staff')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from staff.models import Staff
from workassignment.forms import WorkAssignmentForm

@login_required
def search_staff_by_code(request):
    staff = None
    form = None
    staff_code = request.POST.get('staff_code', '')

    if request.method == 'POST':
        staff = Staff.objects.filter(staff_code=staff_code).first()
        if staff:
            if 'task_title' in request.POST:
                form = WorkAssignmentForm(request.POST, request.FILES)
                if form.is_valid():
                    assignment = form.save(commit=False)
                    assignment.assigned_to = staff
                    assignment.save()
                    messages.success(request, "✅ Work assignment added successfully.")
                    return redirect('search_staff_by_code')
                else:
                    messages.error(request, "⚠️ Please correct the errors below.")
            else:
                form = WorkAssignmentForm()
        else:
            messages.error(request, "⚠️ Staff not found.")
    return render(request, 'staff/search_staff_code.html', {
        'staff': staff,
        'form': form,
        'staff_code': staff_code
    })
