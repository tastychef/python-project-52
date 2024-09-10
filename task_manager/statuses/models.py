from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class TaskStatus(models.Model):
    name = models.CharField(_("name"), max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("statuses:main")

    def __str__(self) -> str:
        return self.name
