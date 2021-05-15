""" views_index.py todolistapp homepage view

__project__ = "CyberSmart Technical Challenge"
__author__ = "Joseph Sarsfield"
__email__ = "joe.sarsfield@gmail.com"
"""

from django.shortcuts import render, HttpResponseRedirect


def index(request):
    return render(request, "index.html", {"todolist": None, "tasks": None})
