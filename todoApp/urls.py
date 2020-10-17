from django.urls import path
from . import views

urlpatterns = [
		path('', views.home, name = 'task-home'),		
		path('update_task/<int:pk>', views.updateTask, name = 'task-update'),
		path('delete_task/<int:pk>', views.deleteTask, name = 'task-delete'),
]