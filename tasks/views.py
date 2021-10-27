from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from .models import TaskModel


@login_required
def home(request):
	if request.method == "POST":
		new_task = TaskModel()
		new_task.user = request.user
		new_task.title = request.POST["title"]
		new_task.save()

	context = {}
	tasks = TaskModel.objects.filter(user=request.user)
	context["tasks"] = tasks
	return render(request, "tasks/home.html", context)



def delete(request, pk):
	try:
		task = TaskModel.objects.get(pk=pk)
		task.delete()
		return redirect('home')
	except TaskModel.DoesNotExist:
		return redirect("home")


def update(request, pk):
	if request.method == "POST":
		task = TaskModel.objects.get(pk=pk)
		task.title = request.POST["title"]
		task.description = request.POST["description"]
		task.save()

	return redirect("home")



def complete(request, pk):
	task = TaskModel.objects.get(pk=pk)
	task.complete = True
	task.save()
	return redirect("home")



def not_complete(request, pk):
	task = TaskModel.objects.get(pk=pk)
	task.complete = False
	task.save()
	return redirect("home")



def clear(request):
	tasks = TaskModel.objects.filter(user=request.user)
	for task in tasks: task.delete()
	return redirect("home")

