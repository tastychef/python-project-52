from django import forms
from django.utils.translation import gettext as _
from django_filters.filters import BooleanFilter, CharFilter, ModelChoiceFilter
from django_filters.filterset import FilterSet

from task_manager.labels.models import Label
from task_manager.tasks.models import Task


class TaskFilter(FilterSet):
    name = CharFilter(lookup_expr="icontains")

    self_tasks = BooleanFilter(
        widget=forms.CheckboxInput,
        field_name="creator",
        method="show_self_tasks",
        label=_("Only my tasks"),
    )

    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name="labels",
        label=_("Label"),
    )

    def show_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(creator=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ("name", "status", "executor", "self_tasks", "labels")
