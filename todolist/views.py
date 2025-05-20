from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    return redirect('tasks')

def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, "todolist/tasks.html", context)

def single_task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, "todolist/task.html", context)

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'todolist/add_task.html', context)

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    context = {'form': form, 'task': task}
    return render(request, 'todolist/edit_task.html', context)

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('tasks')
    context = {'task': task}
    return render(request, 'todolist/delete_task.html', context)

def about(request):
    return render(request, 'todolist/about.html')