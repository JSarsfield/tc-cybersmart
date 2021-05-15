""" test_api.py tests for models go here

__project__ = "CyberSmart Technical Challenge"
__author__ = "Joseph Sarsfield"
__email__ = "joe.sarsfield@gmail.com"
"""

from django.test import TestCase
from todolistapp.models import TodoList, Task

class TodoListTestCase(TestCase):
    """Test cases for TodoList model go here."""

    def setUp(self):
        self.title = "Places to visit."
        todolist = TodoList.objects.create(title=self.title)
        self.pk = todolist.pk

    def test_todolist_read(self):
        """Todolist read"""
        todolist = TodoList.objects.get(pk=self.pk)
        self.assertEqual(todolist.title, self.title)

    def test_todolist_update(self):
        """Todolist update"""
        updated_title = "My updated title."
        todolist = TodoList.objects.create(
            title="Places to visit.")
        TodoList.objects.filter(pk=todolist.pk).update(title=updated_title)
        self.assertEqual(TodoList.objects.get(
            pk=todolist.pk).title, updated_title)

    def test_todolist_delete(self):
        """Todolist delete"""
        todolist = TodoList.objects.create(
            title="Places to visit.")
        TodoList.objects.filter(pk=todolist.pk).delete()
        self.assertRaises(TodoList.DoesNotExist,
                          lambda: TodoList.objects.get(pk=todolist.pk))


class TaskTestCase(TestCase):
    """Test cases for Task model go here."""

    def setUp(self):
        self.todolist = TodoList.objects.create(title="Places to visit.")

    def test_task_create_read(self):
        """Task read"""
        task_title = "Paris"
        task1 = Task.objects.create(
            title=task_title, todolist=self.todolist)
        task1 = Task.objects.get(title="Paris")
        self.assertEqual(task1.title, task_title)
        self.assertEqual(task1.todolist, self.todolist)

    def test_task_update(self):
        """Task update"""
        updated_title = "New York"
        task2 = Task.objects.create(
            title="London", todolist=self.todolist)
        Task.objects.filter(pk=task2.pk).update(title=updated_title)
        self.assertEqual(Task.objects.get(pk=task2.pk).title, updated_title)

    def test_task_delete(self):
        """Task delete"""
        task = Task.objects.create(
            title="London", todolist=self.todolist)
        Task.objects.filter(pk=task.pk).delete()
        self.assertRaises(Task.DoesNotExist,
                          lambda: Task.objects.get(pk=task.pk))