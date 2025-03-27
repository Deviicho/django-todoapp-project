from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import List , Task
from django.http import JsonResponse


# Create your views here.
@login_required
def main(request):
    if request.method == 'POST':
        list_name = request.POST.get("list_name")
        if list_name:
            if not List.can_user_create_list(request.user):
                return JsonResponse({"error": "Maximum number of lists reached."}, status=400)
            try:
                # Attempt to create the list
                List.objects.create(name=list_name, its_User=request.user)
            except:
                # Handle the case where the list name already exists for the user
                messages.error(request, f'A list with the name "{list_name}" already exists.')
            return redirect('main')  # Redirect to avoid duplicate submissions
    
    
    list = List.objects.all()
    context = {'list' : list.filter(its_User = request.user)}
    return render(request , 'main_page/mainpage.html' , context) 



@login_required
def taskview(request, list_id):
    todo_list = get_object_or_404(List, id=list_id, its_User=request.user)# needs to understand more
    
    task = Task.objects.all()
    context = {'todo_list': todo_list,
               'task' : task.filter(its_List=todo_list)}
            #    'task' : task.filter(its_list=todo_list)
    return render(request, 'main_page/Taskview.html', context)

@login_required
def delete_list(request , list_id):
    
    todo_list = get_object_or_404(List, id=list_id, its_User=request.user)
    
    todo_list.delete()
    
    return render(request, 'main_page/Taskview.html')

@login_required
def add_task(request , list_id):
    todo_list = get_object_or_404(List, id=list_id, its_User=request.user)
    
    # Check if the list can accept more tasks
    if not todo_list.can_add_task():
        return JsonResponse({"error": "Maximum number of tasks reached for this list."}, status=400)
    
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        if task_name:
            try:
                Task.objects.create(name=task_name , is_checked=False , its_List=todo_list)
            except:
                messages.error(request, f'A task with the name "{task_name}" already exists.')
    task = Task.objects.all()
    context = {'todo_list': todo_list,
               'task' : task.filter(its_List=todo_list)}
    
    return render(request, 'main_page/Taskview.html' , context)


@login_required
def delete_task(request , list_id , task_id):
    
    todo_list = get_object_or_404(List, id=list_id, its_User=request.user)
    
    task = get_object_or_404(Task, id=task_id, its_List=todo_list)
    
    task.delete()
    
    return redirect('taskview', list_id=list_id)

@login_required
def toggle_task(request, list_id, task_id):
    todo_list = get_object_or_404(List, id=list_id, its_User=request.user)
    task = get_object_or_404(Task, id=task_id, its_List=todo_list)
    
    if request.method == 'POST':
        # Update the is_checked field based on the checkbox state
        task.is_checked = 'is_checked' in request.POST  # True if checkbox is checked, False otherwise
        task.save()
    
    # Redirect back to the task list
    return redirect('taskview', list_id=list_id)
