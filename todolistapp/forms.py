from django.forms import ModelForm
from .models import TodoList, Task


class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ["title"]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task_done"]
