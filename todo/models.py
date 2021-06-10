from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Todo(models.Model):

    title = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField()
    favorite = models.BooleanField()

    list = models.ForeignKey('TodoList', on_delete=CASCADE)


class TodoList(models.Model):

    name = CharField(max_length=255)

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'