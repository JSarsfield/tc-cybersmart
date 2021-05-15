from django.contrib import admin
from . import models

# Register your models here.


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "task_done",  "created")


admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Task, TaskAdmin)
