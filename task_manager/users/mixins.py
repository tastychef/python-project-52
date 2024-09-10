from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class CheckRelatedTasksMixin:

    def post(self, request, *args, **kwargs):
        if (
            self.get_object().tasks_where_creator.all().exists()
            or self.get_object().tasks_where_executor.all().exists()
        ):
            messages.error(
                self.request, _("Unable to delete user because it is in use")
            )
            return redirect("users:main")

        return super().post(request, *args, **kwargs)
