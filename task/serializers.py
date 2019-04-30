from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    expire_date = serializers.DateField(format='%Y-%m-%d')
    class Meta:
        model = Task
        fields = ['id','content','create_date', 'expire_date','status','priority']