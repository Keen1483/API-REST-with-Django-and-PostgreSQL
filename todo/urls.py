from rest_framework import routers

from todo.views import TodoListViewSet, TodoViewSet


router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
router.register('todo-list', TodoListViewSet)