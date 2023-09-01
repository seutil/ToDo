from django import forms

from .models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'task-name',
                'class': 'form-control',
            })
        }
