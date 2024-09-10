from django.urls import path

from task_manager.tasks.views import (TaskCreateView, TaskDeleteView,
                                      TaskDetail, TaskListView, TaskUpdateView)

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="main"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="update"),
    path("<int:pk>/", TaskDetail.as_view(), name="detail"),
]
