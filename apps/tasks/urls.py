from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('home', views.Home, name='home'),
    path('tasks/create', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks', views.TaskListView, name='tasks'),
    path('tasks/upcoming', views.UpcomingTaskView, name='tasks-upcoming'),
    path('tasks/completed', views.CompletedTaskView, name='task-completed'),
    path('tasks/<slug:slug>', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<slug:slug>/update', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<slug:slug>/delete', views.TaskDeleteView.as_view(), name='task-delete'),
]