from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    def get_absolute_url(self):
        return reverse("users:main")

    @property
    def full_name(self) -> str:
        return self.get_full_name()

    def __str__(self) -> str:
        return self.full_name
