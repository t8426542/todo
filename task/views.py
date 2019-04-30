from django.http import HttpResponse
from rest_framework import mixins, viewsets

from task.models import Task
from task.serializers import TaskSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the task index.")


class TaskView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


