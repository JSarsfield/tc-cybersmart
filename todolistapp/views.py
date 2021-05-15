""" views_index.py todolistapp homepage view

__project__ = "CyberSmart Technical Challenge"
__author__ = "Joseph Sarsfield"
__email__ = "joe.sarsfield@gmail.com"
"""

from django.shortcuts import redirect, render, HttpResponseRedirect
from todolistapp.models import TodoList, Task
from todolistapp.forms import TodoListForm


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
    if request.method == "POST":
        todolist = TodoList.objects.get(pk=pk)
        form = TodoListForm(request.POST, instance=todolist)
        if form.is_valid():
            form.save()
            return redirect(".")
    else:
        form = TodoListForm()
    return render(request,
                  "todolist_update.html",
                  {"form": form}
                  )


def todolist_delete(request, pk):
    """Delete todolist view"""
    TodoList.objects.filter(pk=pk).delete()
    return redirect("/")
