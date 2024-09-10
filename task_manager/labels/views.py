from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.forms import LabelCreateUpdateForm
from task_manager.labels.mixins import CheckRelatedTasksMixin
from task_manager.labels.models import Label
from task_manager.mixins import AuthRequiredMixin, NoPermissionRedirectMixin


class LabelCreateView(
    NoPermissionRedirectMixin, AuthRequiredMixin, SuccessMessageMixin, CreateView
):
    model: Label = Label
    form_class: LabelCreateUpdateForm = LabelCreateUpdateForm
    template_name: str = "labels/create.html"

    success_message: tuple = _("Label successfully created")


class LabelListView(NoPermissionRedirectMixin, AuthRequiredMixin, ListView):
    model: Label = Label
    template_name: str = "labels/index.html"


class LabelUpdateView(
    NoPermissionRedirectMixin, AuthRequiredMixin, SuccessMessageMixin, UpdateView
):
    model: Label = Label
    form_class: LabelCreateUpdateForm = LabelCreateUpdateForm
    template_name: str = "labels/update.html"

    success_message: tuple = _("Label successfully updated")


class LabelDeleteView(
    NoPermissionRedirectMixin,
    AuthRequiredMixin,
    CheckRelatedTasksMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model: Label = Label
    template_name: str = "labels/delete.html"

    success_message: tuple = _("Label successfully deleted")
    success_url = reverse_lazy("labels:main")
