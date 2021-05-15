""" views_index.py todolistapp homepage view

__project__ = "CyberSmart Technical Challenge"
__author__ = "Joseph Sarsfield"
__email__ = "joe.sarsfield@gmail.com"
"""

from django.shortcuts import redirect, render, HttpResponseRedirect
from todolistapp.models import TodoList, Task
from todolistapp.forms import TodoListForm, TaskForm
from .api import get_temperature, get_geolocation_from_ip


def index(request):
    """Homepage view"""
    todolists = TodoList.objects.all()
    return render(request, "home.html", {"todolists": todolists})


def todolist_create(request):
    """Create todolists list"""
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TodoListForm()
    return render(request,
                  "todolist_create.html",
                  {"form": form}
                  )


def todolist_update(request, pk):
    """Update todolists view and add tasks"""
    todolist = TodoList.objects.get(pk=pk)
    return render(request,
                  "todolist_update.html",
                  {"todolist": todolist, "tasks": todolist.tasks.all()},
                  )


def todolist_delete(request, pk):
    """Delete todolist view"""
    TodoList.objects.filter(pk=pk).delete()
    return redirect("/")


def task_create(request, pk):
    """Create task"""
    location = get_geolocation_from_ip(request)
    todolist = TodoList.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        form.instance.todolist = todolist
        if form.is_valid():
            form.save()
            return redirect("/todolist/update/"+pk)
    else:
        form = TaskForm()
    return render(request,
                  "task_create.html",
                  {"form": form}
                  )


def task_update(request, todo_pk, pk):
    """Update todolists view and add tasks"""
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        form.instance.temperature = get_temperature(form.instance.location)
        if form.is_valid():
            form.save()
            return redirect("/todolist/update/"+todo_pk)
    else:
        form = TaskForm(initial={'title': task.title,
                                 'location': task.location,
                                 'temperature': task.temperature,
                                 'task_done': task.task_done})
    return render(request,
                  "task_update.html",
                  {"form": form, "task": task},
                  )


def task_delete(request, todo_pk, pk):
    """Delete todolist view"""
    Task.objects.filter(pk=pk).delete()
    return redirect("/todolist/update/"+todo_pk)
