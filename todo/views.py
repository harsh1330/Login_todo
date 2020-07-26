from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from . froms import TaskForm

# Create your views here.

def todo(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    
    context={
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
    return redirect('/todo/')

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/todo/')