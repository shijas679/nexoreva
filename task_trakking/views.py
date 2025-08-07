from django.shortcuts import render
from staff.models import Staff
from workassignment.models import WorkAssignment

# Create your views here.

def task_status(request):
    error_message = None
    assigned_tasks = None

    if request.method == "POST":
        staff_code = request.POST.get('staff_code', '').strip()

        if staff_code:
            try:
                staff_obj = Staff.objects.get(staff_code=staff_code)
                assigned_tasks = staff_obj.assignments.all()

                if 'update' in request.POST:
                    # Loop through tasks and update their statuses
                    for task in assigned_tasks:
                        selected_status = request.POST.get(f'status_{task.id}')
                        if selected_status and selected_status != task.status:
                            task.status = selected_status
                            task.save()
                # If 'fetch' is clicked, just fetch and display the tasks — no update
                elif 'fetch' in request.POST:
                    pass  # Tasks are already fetched above

            except Staff.DoesNotExist:
                error_message = "No staff found with this code."
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
        else:
            error_message = "Please enter a staff code."

    return render(request, 'task_trakking/task_status.html', {
        'assigned_tasks': assigned_tasks,
        'error_message': error_message
    })
