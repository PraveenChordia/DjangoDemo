from django.shortcuts import render
from Demo.models import Task
from Demo.forms import TaskForm


# Create your views here.
def new_task(request):
    context = {}
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context['form'] = form
    form = TaskForm()
    return render(request, 'tasks.html', {'form': form})


def all_task(request):
    data = Task.objects.all()
    context = {'data': data}
    return render(request, 'all_tasks.html', context)
