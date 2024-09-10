from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class CheckRelatedTasksMixin:

    def post(self, request, *args, **kwargs):
        if self.get_object().tasks.all().exists():
            messages.error(
                self.request, _("Unable to delete status because it is in use")
            )
            return redirect("statuses:main")

        return super().post(request, *args, **kwargs)
