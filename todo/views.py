from django.db.models import query
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from todo.models import Todo, TodoList
from todo.serializers import TodoListSerializer, TodoSerializer
from rest_framework.permissions import IsAuthenticated


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['due_date', 'completed', 'favorite']
    search_fields = ['title']

class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated, )