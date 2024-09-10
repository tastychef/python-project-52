from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class InfoMessageMixin:
    info_message = None

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.message)
        return super().dispatch(request, *args, **kwargs)


class NoPermissionRedirectMixin:

    def handle_no_permission(self, permission_denied_message, permission_denied_url):
        messages.error(self.request, permission_denied_message)
        return redirect(permission_denied_url)


class AuthRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission(
                _("You are not logged in! Please sign in"), "login"
            )
        return super().dispatch(request, *args, **kwargs)


class CheckSelfUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object() == self.request.user:
            return self.handle_no_permission(
                self.permission_denied_message, "users:main"
            )
        return super().dispatch(request, *args, **kwargs)
