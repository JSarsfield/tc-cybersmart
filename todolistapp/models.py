""" models.py todolistapp models go here

__project__ = "CyberSmart Technical Challenge"
__author__ = "Joseph Sarsfield"
__email__ = "joe.sarsfield@gmail.com"
"""

from todolistapp.api import get_temperature
from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    """TodoList model stores a list of tasks.
    This model has a one-to-many relationship with Task model."""
    title = models.CharField(max_length=255)  # Title of TodoList

    def __str__(self):
        return self.title


class Task(models.Model):
    """Task model must belong to a ToDoList.
    This model has a many-to-one relationship with TodoList model."""

    class TempBackgroundColour(models.TextChoices):
        COLD = 'CD', '#0000FF',
        WARM = 'WM', '#FFA500'
        HOT = 'HT', '#FF0000'
        DEFAULT = 'DT', '#FFFFFF'

    title = models.CharField(max_length=128)  # Title of Task
    location = models.CharField(max_length=128, default="london")  # Location
    temperature = models.FloatField(
        null=True, blank=True)  # Temperature in celsius
    bg_colour = models.CharField(
        max_length=2,
        choices=TempBackgroundColour.choices,
        default=TempBackgroundColour.DEFAULT
    )  # Task background color
    todolist = models.ForeignKey(
        'TodoList',
        on_delete=models.CASCADE,
        related_name='tasks'
    )  # Many-to-one relationship with TodoList model.
    task_done = models.BooleanField(default=False)  # Toggle task complete
    created = models.DateField(default=timezone.now)

    class Meta:
        ordering = ["-created"]  # order fields chronologically

    def __str__(self):
        return self.title
