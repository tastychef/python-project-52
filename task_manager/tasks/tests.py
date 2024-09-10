from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import TaskStatus
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.utils import get_test_data


class TaskTest(TestCase):
    fixtures = [
        "users.json",
        "task_statuses.json",
        "labels.json",
        "tasks.json",
        "tasks_to_labels.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.test_data = get_test_data()

    def setUp(self):
        exist_user_data = self.test_data["users"]["existing"]
        self.client.login(
            username=exist_user_data["username"],
            password=exist_user_data["password"],
        )

    def assertTask(self, task, task_data):
        self.assertEqual(task.__str__(), task_data["name"])
        self.assertEqual(task.description, task_data["description"])
        self.assertEqual(task.status.pk, task_data["status"])
        self.assertEqual(task.creator.pk, task_data["creator"])
        self.assertEqual(task.executor.pk, task_data["executor"])
        task_labels = list(map(lambda label: label.pk, task.labels.all()))
        self.assertEqual(task_labels, task_data["labels"])

    def test_main_page(self):
        response = self.client.get(reverse("tasks:main"))
        self.assertEqual(response.status_code, 200)

        tasks = Task.objects.all()
        self.assertQuerysetEqual(
            response.context["task_list"],
            tasks,
            ordered=False,
        )

    def test_create_page(self):
        response = self.client.get(reverse("tasks:create"))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        new_task_data = self.test_data["tasks"]["new"]
        response = self.client.post(reverse("tasks:create"), new_task_data)

        self.assertRedirects(response, reverse("tasks:main"))
        created_task = Task.objects.get(name=new_task_data["name"])
        self.assertTask(created_task, new_task_data)

    def test_update_page(self):
        exist_task_data = self.test_data["tasks"]["existing"]
        exist_task = Task.objects.get(name=exist_task_data["name"])
        response = self.client.get(reverse("tasks:update", args=[exist_task.pk]))

        self.assertEqual(response.status_code, 200)

    def test_update(self):
        exist_task_data = self.test_data["tasks"]["existing"]
        new_task_data = self.test_data["tasks"]["new"]
        exist_task = Task.objects.get(name=exist_task_data["name"])
        response = self.client.post(
            reverse("tasks:update", args=[exist_task.pk]),
            new_task_data,
        )

        self.assertRedirects(response, reverse("tasks:main"))
        updated_task = Task.objects.get(name=new_task_data["name"])
        self.assertTask(updated_task, new_task_data)

    def test_delete_page(self):
        exist_task_data = self.test_data["tasks"]["existing"]
        exist_task = Task.objects.get(name=exist_task_data["name"])
        response = self.client.get(reverse("tasks:delete", args=[exist_task.pk]))

        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        exist_task_data = self.test_data["tasks"]["existing"]
        exist_task = Task.objects.get(name=exist_task_data["name"])
        response = self.client.post(reverse("tasks:delete", args=[exist_task.pk]))

        self.assertRedirects(response, reverse("tasks:main"))
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(name=exist_task_data["name"])

    def test_filter(self):
        exist_user_data = self.test_data["users"]["existing"]
        exist_user = User.objects.get(username=exist_user_data["username"])

        filterset = {"self_tasks": "on"}
        response = self.client.get(reverse("tasks:main"), filterset)
        tasks = Task.objects.filter(creator=exist_user.pk)
        self.assertQuerysetEqual(response.context["task_list"], tasks)

        exist_status_data = self.test_data["statuses"]["existing"]
        exist_status = TaskStatus.objects.get(name=exist_status_data["name"])

        filterset = {"status": exist_status.pk}
        response = self.client.get(reverse("tasks:main"), filterset)
        tasks = Task.objects.filter(**filterset)
        self.assertQuerysetEqual(response.context["task_list"], tasks)

        filterset = {"self_tasks": "on", "status": exist_status.pk}
        response = self.client.get(reverse("tasks:main"), filterset)
        self.assertQuerysetEqual(response.context["task_list"], [])
