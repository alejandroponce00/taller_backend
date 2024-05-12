from rest_framework import routers
from .api import TaskViewSet

routers= routers.DefaultRouter()
routers.register('api/tasks', TaskViewSet, 'tasks')

urlpatterns = routers.urls
