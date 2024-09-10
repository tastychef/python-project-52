from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import AuthRequiredMixin, NoPermissionRedirectMixin
from task_manager.statuses.forms import TaskStatusCreateUpdateForm
from task_manager.statuses.mixins import CheckRelatedTasksMixin
from task_manager.statuses.models import TaskStatus


class TaskStatusCreateView(
    NoPermissionRedirectMixin, AuthRequiredMixin, SuccessMessageMixin, CreateView
):
    model: TaskStatus = TaskStatus
    form_class: TaskStatusCreateUpdateForm = TaskStatusCreateUpdateForm
    template_name: str = "statuses/create.html"

    success_message: tuple = _("Status successfully created")


class TaskStatusListView(NoPermissionRedirectMixin, AuthRequiredMixin, ListView):
    model: TaskStatus = TaskStatus
    template_name: str = "statuses/index.html"


class TaskStatusUpdateView(
    NoPermissionRedirectMixin, AuthRequiredMixin, SuccessMessageMixin, UpdateView
):
    model: TaskStatus = TaskStatus
    form_class: TaskStatusCreateUpdateForm = TaskStatusCreateUpdateForm
    template_name: str = "statuses/update.html"

    success_message: tuple = _("Status successfully updated")


class TaskStatusDeleteView(
    NoPermissionRedirectMixin,
    AuthRequiredMixin,
    CheckRelatedTasksMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model: TaskStatus = TaskStatus
    template_name: str = "statuses/delete.html"

    success_message: tuple = _("Status successfully deleted")
    success_url = reverse_lazy("statuses:main")
