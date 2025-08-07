from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from staff.models import Staff
from .models import WorkAssignment
from .forms import WorkAssignmentForm


# Home View – List All Active Interns and Employees
def home(request):
    users = Staff.objects.filter(role__in=['Intern', 'Employee'], status='Active')
    return render(request, 'workassignment/user_list.html', {'users': users})


# User Detail – View Individual Staff & Their Assignments
def user_detail(request, user_id):
    user = get_object_or_404(Staff, id=user_id)
    assignments = WorkAssignment.objects.filter(assigned_to=user)
    return render(request, 'workassignment/user_detail.html', {
        'user': user,
        'assignments': assignments
    })


#  Add Assignment for Specific User
def add_assignment(request, user_id):
    user = get_object_or_404(Staff, id=user_id)
    if request.method == 'POST':
        form = WorkAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.assigned_to = user
            assignment.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = WorkAssignmentForm()
    return render(request, 'workassignment/add_assignment.html', {
        'form': form,
        'user': user
    })


# Admin View: List of Users with Assigned Work
@login_required
def viewwork_assignment_userlist_staff(request):
    users = Staff.objects.filter(role__in=['Intern', 'Employee'], status='Active')
    user_data = []
    for user in users:
        assignments = WorkAssignment.objects.filter(assigned_to=user)
        for assign in assignments:
            user_data.append({
                'id': user.id,
                'unicode': user.staff_code,
                'username': user.full_name,
                'role': user.role,
                'assignment': assign.task_title,
                'status': assign.status,  # You can update this if WorkAssignment has a real status field
                'assignment_id': assign.id
            })
    return render(request, 'workassignment/assignment_userlist.html', {
        'user_data': user_data
    })

# Add Assignment via Staff Code (Search + Assign Form)
@login_required
def add_assignment_view(request, user_id):
    staff = None
    staff_code = ''
    form = WorkAssignmentForm()

    if request.method == 'POST':
        staff_code = request.POST.get('staff_code', '').strip()

        # Searching by Staff Code
        if 'staff_code' in request.POST and 'assigned_to' not in request.POST:
            if staff_code:
                try:
                    staff = Staff.objects.get(staff_code=staff_code)
                except Staff.DoesNotExist:
                    staff = None
            form = WorkAssignmentForm()

        # Submitting assignment form
        elif 'assigned_to' in request.POST:
            staff_id = request.POST.get('assigned_to')
            try:
                staff = Staff.objects.get(id=staff_id)
            except Staff.DoesNotExist:
                staff = None

            form = WorkAssignmentForm(request.POST, request.FILES)
            if form.is_valid() and staff:
                assignment = form.save(commit=False)
                assignment.assigned_to = staff
                assignment.save()
                return redirect('viewwork_assignment_userlist_staff')  # Moved inside success condition

    return render(request, 'workassignment/add_assignment.html', {
        'form': form,
        'staff': staff,
        'staff_code': staff_code,
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import WorkAssignment
from .forms import WorkAssignmentForm

# Edit Assignment

def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(WorkAssignment, id=assignment_id)
    if request.method == 'POST':
        form = WorkAssignmentForm(request.POST, request.FILES, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('viewwork_assignment_userlist_staff')
    else:
        form = WorkAssignmentForm(instance=assignment)
    return render(request, 'workassignment/edit_assignment.html', {'form': form})

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(WorkAssignment, id=assignment_id)
    assignment.delete()
    return redirect('viewwork_assignment_userlist_staff')

#  Delete Assignment
@login_required
def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(WorkAssignment, id=assignment_id)

    if request.method == 'POST':
        assignment.delete()
        return redirect('viewwork_assignment_userlist_staff')

    return render(request, 'workassignment/confirm_delete.html', {
        'assignment': assignment
    })
