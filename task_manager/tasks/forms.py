import django.forms as forms

from task_manager.tasks.models import Task


class TaskCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description", "status", "executor", "labels")
