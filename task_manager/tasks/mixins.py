from django.utils.translation import gettext as _


class CheckIsUserTaskCreatorMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().creator == self.request.user:
            return self.handle_no_permission(
                _("A task can only be deleted by its author"), "tasks:main"
            )
        return super().dispatch(request, *args, **kwargs)