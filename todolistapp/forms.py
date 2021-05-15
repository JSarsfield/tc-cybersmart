from django.forms import ModelForm
from .models import TodoList, Task


class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ["title"]


class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        fields = ["title", "location", "task_done"]
