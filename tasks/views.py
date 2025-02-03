from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Task
from .forms import TaskForm

def task_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort_by', 'deadline')
    tasks = Task.objects.all()
    
    if search_query:
        tasks = tasks.filter(description__icontains=search_query)
    
    if sort_by in ['deadline', 'status', 'priority']:
        tasks = tasks.order_by(sort_by)
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def pending_tasks(request):
    tasks = Task.objects.filter(status='pending')
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter': 'pending'})

def completed_tasks(request):
    tasks = Task.objects.filter(status='completed')
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter': 'completed'})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
