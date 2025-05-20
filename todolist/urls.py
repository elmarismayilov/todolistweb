from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks/<int:task_id>', views.single_task, name="single_task"),
    path('add_task', views.add_task, name="add_task"),
    path('tasks/<int:task_id>/edit', views.edit_task, name="edit_task"),
    path('tasks/<int:task_id>/delete', views.delete_task, name="delete_task"),
    path('about/', views.about, name='about'),
]