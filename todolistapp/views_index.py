""" views_index.py todolistapp homepage view

__project__ = "CyberSmart Technical Challenge"
__author__ = "Joseph Sarsfield"
__email__ = "joe.sarsfield@gmail.com"
"""

from django.shortcuts import render, HttpResponseRedirect
from .models import TodoList, Task


def index(request):
    if request.method == "POST":
        action = request.POST.get("action", "None")
        if action == "AddTodo":
            title = request.POST.get("title", None)
            if title:
                TodoList.objects.create(title=title)
            return HttpResponseRedirect("/")
    return render(request, "index.html", {"todolist": None, "tasks": None})
