from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =('id','vehiculo','dueño','falla','reparado','fecha')  
        read_only_fields =('id' ,'fecha')  
        