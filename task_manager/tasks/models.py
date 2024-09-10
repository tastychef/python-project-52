from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import TaskStatus


class Task(models.Model):
    name = models.CharField(_("name"), max_length=150, unique=True)
    description = models.TextField(_("description"), blank=True)
    status = models.ForeignKey(
        TaskStatus,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name=_("status"),
    )
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name="tasks_where_creator",
        verbose_name=_("creator"),
    )
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name="tasks_where_executor",
        blank=True,
        null=True,
        verbose_name=_("executor"),
    )
    labels = models.ManyToManyField(
        Label,
        through="TaskToLabel",
        related_name="tasks",
        blank=True,
        verbose_name=_("labels"),
    )

    def get_absolute_url(self):
        return reverse("tasks:main")

    def __str__(self) -> str:
        return self.name


class TaskToLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
