from django.urls import path
from . import views

urlpatterns = [
    path('' , views.main , name='main'),
    path('taskview/<int:list_id>/' , views.taskview , name='taskview'),# needs to understand more
    path('delete_list/<int:list_id>/delete/', views.delete_list, name='delete_list'),# needs to understand more
    path('add_task/<int:list_id>' , views.add_task , name='add_task'),
    path('delete_task/<int:list_id>/<int:task_id>/delete/' , views.delete_task , name='delete_task'),
    path('toggle_task/<int:list_id>/<int:task_id>/', views.toggle_task, name='toggle_task'),
]
