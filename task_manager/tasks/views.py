from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.mixins import AuthRequiredMixin, NoPermissionRedirectMixin
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskCreateUpdateForm
from task_manager.tasks.mixins import CheckIsUserTaskCreatorMixin
from task_manager.tasks.models import Task


class TaskCreateView(
    NoPermissionRedirectMixin, AuthRequiredMixin, SuccessMessageMixin, CreateView
):
    model = Task
    form_class = TaskCreateUpdateForm
    template_name = "tasks/create.html"
    success_message = _("Task successfully created")

    def form_valid(self, form: TaskCreateUpdateForm):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskListView(NoPermissionRedirectMixin, AuthRequiredMixin, FilterView):
    model = Task
    template_name = "tasks/index.html"
    filterset_class = TaskFilter


class TaskUpdateView(
    NoPermissionRedirectMixin, AuthRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Task
    form_class: TaskCreateUpdateForm = TaskCreateUpdateForm
    template_name = "tasks/update.html"

    success_message = _("Task successfully updated")


class TaskDeleteView(
    NoPermissionRedirectMixin,
    AuthRequiredMixin,
    CheckIsUserTaskCreatorMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Task
    template_name = "tasks/delete.html"

    success_message = _("Task successfully deleted")
    success_url = reverse_lazy("tasks:main")


class TaskDetail(NoPermissionRedirectMixin, AuthRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
