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
<<<<<<< HEAD
=======

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
>>>>>>> f5cf8ae058cc2e7ce1a8dfe72ade2f7808dec3c4
