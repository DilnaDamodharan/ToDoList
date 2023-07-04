from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from ToDoApp.forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        task = Task(name=name, priority=priority)
        task.save()

    tasks = Task.objects.all()
    return render(request, 'home.html', {'task': tasks})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})

class TaskListview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',Kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
