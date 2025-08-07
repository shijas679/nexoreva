
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StaffForm
from .models import Staff
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            staff = form.save(commit=False)

            # Auto-generate staff_code only on creation
            if not staff.staff_code:
                prefix = 'nxrint' if staff.role == 'Intern' else 'nxremp'
                while True:
                    code = generate_unique_code(prefix)
                    if not Staff.objects.filter(staff_code=code).exists():
                        staff.staff_code = code
                        break

            staff.save()
            messages.success(request, "✅ Staff member added successfully.")
            return redirect('view_staff')
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:


        form = StaffForm()

    return render(request, 'staff/add_staff.html', {'form': form})

@login_required
def view_staff(request):
    staff_list = Staff.objects.all().order_by('-id')  # Latest first
    return render(request, 'staff/view_staff.html', {'staff_list': staff_list})

@login_required
def edit_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            # Prevent staff_code from being updated
            updated_staff = form.save(commit=False)
            updated_staff.staff_code = staff.staff_code  # keep old code
            updated_staff.save()
            messages.success(request, "✅ Staff details updated successfully.")
            return redirect('view_staff')
        else:
            messages.error(request, "⚠️ Please correct the errors.")
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff/edit_staff.html', {'form': form, 'staff': staff})

@login_required
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    staff.delete()
    messages.success(request, "🗑️ Staff member deleted successfully.")
    return redirect('view_staff')

from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def view_staff(request):
    staff_list = Staff.objects.all().order_by('-id')  # default list

    # Filter by role
    role_filter = request.GET.get('sort', '')
    if role_filter in ['Employee', 'Intern']:
        staff_list = staff_list.filter(role=role_filter)
    # if role_filter is 'All' or empty, show all (no filter)

    # Search by name, email, or Unicode (staff_code)
    query = request.GET.get('search', '')
    if query is None or query.lower() == 'none':
        query = ''

    if query:
        staff_list = staff_list.filter(
            Q(full_name__icontains=query) |
            Q(email__icontains=query) |
            Q(staff_code__icontains=query)
        )

    return render(request, 'staff/view_staff.html', {
        'staff_list': staff_list,
        'selected_role': role_filter,
        'search_query': query  # Send cleaned query string
    })

from django.shortcuts import render

def search_staff_by_code(request):
    # Temporary implementation to fix import error
    return render(request, 'staff/search.html')
