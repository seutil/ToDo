from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {
        'tasks': tasks,
    })
