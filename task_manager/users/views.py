from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import (AuthRequiredMixin, CheckSelfUserMixin,
                                 NoPermissionRedirectMixin)
from task_manager.users.forms import UserCreateUpdateForm
from task_manager.users.mixins import CheckRelatedTasksMixin


class UserCreateView(SuccessMessageMixin, CreateView):
    model: User = get_user_model()
    form_class: UserCreateUpdateForm = UserCreateUpdateForm
    template_name: str = "users/create.html"

    success_message: tuple = _("User successfully registered")
    success_url = reverse_lazy("login")


class UserListView(ListView):
    model: User = get_user_model()
    template_name: str = "users/index.html"


class UserDeleteView(
    NoPermissionRedirectMixin,
    AuthRequiredMixin,
    CheckSelfUserMixin,
    CheckRelatedTasksMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model: User = get_user_model()
    template_name: str = "users/delete.html"

    permission_denied_message: tuple = _("You can't delete another user")

    success_message: tuple = _("User successfully deleted")
    success_url = reverse_lazy("users:main")


class UserUpdateView(
    NoPermissionRedirectMixin,
    AuthRequiredMixin,
    SuccessMessageMixin,
    CheckSelfUserMixin,
    UpdateView,
):
    model: User = get_user_model()
    form_class: UserCreateUpdateForm = UserCreateUpdateForm
    template_name: str = "users/update.html"

    permission_denied_message: tuple = _("You can't update another user")

    success_message: tuple = _("User successfully updated")
