from django import forms
from Demo.models import Task

class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text='Required', label='Name')
    description = forms.CharField(max_length=100, help_text='Required', label='Description')
    email = forms.EmailField(max_length=75, help_text='Required', label='Email')

    class Meta:
        model = Task
        fields = ('name', 'description', 'email')