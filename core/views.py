from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import NewTaskForm


def index(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewTaskForm()

    tasks = Task.objects.all()
    return render(request, 'index.html', {
        'form': form,
        'tasks': tasks,
    })


def close(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.is_closed = True
    task.save()
    return redirect('core:index')


def open(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.is_closed = False
    task.save()
    return redirect('core:index')
