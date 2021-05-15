"""weatherproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolistapp.views import index, todolist_create, todolist_update, todolist_delete, task_create, task_update, task_delete

urlpatterns = [
    path('', index, name="home"),

    path('todolist/create/', todolist_create, name="todolist_create"),
    path('todolist/update/<str:pk>/', todolist_update, name="todolist_update"),
    path('todolist/delete/<str:pk>/', todolist_delete, name="todolist_delete"),

    path('task/create/<str:pk>/', task_create, name="task_create"),
    path('task/update/<str:todo_pk>/<str:pk>/',
         task_update, name="task_update"),
    path('task/delete/<str:todo_pk>/<str:pk>/',
         task_delete, name="task_delete"),


    path('admin/', admin.site.urls),
]
