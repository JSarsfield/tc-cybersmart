""" models.py todolistapp models go here

__project__ = "CyberSmart Technical Challenge"
__author__ = "Joseph Sarsfield"
__email__ = "joe.sarsfield@gmail.com"
"""

from django.dispatch import receiver
from django.db.models.signals import pre_save
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

    class Locations(models.TextChoices):
        LONDON = 'LO', 'London',
        ALASKA = 'AL', 'Alaska',
        NEW_YORK = 'NE', 'New York',
        MOSCOW = 'MO', 'Moscow',
        TOKYO = 'TO', 'Tokyo',
        SHANGHAI = 'SH', 'Shanghai',
        DELHI = 'DE', 'Delhi'
        MECCA = 'ME', 'Mecca'

    title = models.CharField(max_length=128)  # Title of Task
    location = models.CharField(
        max_length=3, choices=Locations.choices, default=Locations.LONDON)  # Location
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


@receiver(pre_save, sender=Task)
def pre_save_task(sender, instance, *args, **kwargs):
    """Set the temperature field based on location and background color"""
    if instance.pk == None or instance.task_done != True or Task.objects.get(pk=instance.pk).task_done != True:  # if not marked as done
        instance.temperature = get_temperature(instance.get_location_display())
    if instance.temperature is None:
        instance.bg_colour = Task.TempBackgroundColour.DEFAULT
    elif instance.temperature < 10:
        instance.bg_colour = Task.TempBackgroundColour.COLD
    elif instance.temperature > 18:
        instance.bg_colour = Task.TempBackgroundColour.HOT
    else:
        instance.bg_colour = Task.TempBackgroundColour.WARM
