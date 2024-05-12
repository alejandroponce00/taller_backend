from rest_framework import viewsets,permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer
    
    @action(detail=True, methods=['post'])
    def reparado(self,request, pk=None):
        task = self.get_object()
        task.reparado = not task.reparado
        task.save()
        return Response({
            'status':'reparado con exito' if task.reparado else 'en reparacion'
            },status= status.HTTP_200_OK)
        status
    