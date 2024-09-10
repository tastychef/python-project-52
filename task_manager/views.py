from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from task_manager.mixins import InfoMessageMixin


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(SuccessMessageMixin, views.LoginView):
    template_name = "login.html"
    success_message = _("You are logged in")


class LogoutView(InfoMessageMixin, views.LogoutView):
    template_name = "logout.html"
    message = _("You are logged out")
