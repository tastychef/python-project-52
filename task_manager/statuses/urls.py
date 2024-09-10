from django.urls import path

from task_manager.statuses.views import (TaskStatusCreateView,
                                         TaskStatusDeleteView,
                                         TaskStatusListView,
                                         TaskStatusUpdateView)

app_name = "statuses"

urlpatterns = [
    path("", TaskStatusListView.as_view(), name="main"),
    path("create/", TaskStatusCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", TaskStatusDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", TaskStatusUpdateView.as_view(), name="update"),
]
