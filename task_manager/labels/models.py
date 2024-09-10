from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(_("name"), max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("labels:main")

    def __str__(self) -> str:
        return self.name
