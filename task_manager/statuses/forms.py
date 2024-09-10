from django.forms import ModelForm

from task_manager.statuses.models import TaskStatus


class TaskStatusCreateUpdateForm(ModelForm):

    class Meta:
        model = TaskStatus
        fields = ("name",)
