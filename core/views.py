from django.shortcuts import render

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
