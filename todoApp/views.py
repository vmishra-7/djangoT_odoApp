from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
def home(request) :
	tasks = Task.objects.all()
	form = TaskForm()
	if request.method == 'POST' :
		form = TaskForm(request.POST)
		if form.is_valid() :
			form.save()
		return redirect('task-home')
	else :
		context = {
			'tasks' : tasks,
			'form' : form,
		}
		return render(request, 'todoApp/home.html', context)


def updateTask(request, pk) :
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST' :
		form = TaskForm(request.POST, instance=task)
		if form.is_valid() :
			form.save()
		return redirect('task-home')
	context = {
		'form' : form
	}
	return render(request, 'todoApp/update_task.html', context)

def deleteTask(request, pk) :
	task = Task.objects.get(id=pk)
	if request.method == 'POST' :
		task.delete()
		return redirect('task-home')
	context = {
		'form' : task
	}
	return render(request, 'todoApp/delete_task.html', context)
# Create your views here.
