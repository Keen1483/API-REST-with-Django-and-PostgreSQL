from datetime import datetime
from todo.models import Todo, TodoList
from django.test import TestCase

# Create your tests here.

class TodoTestCase(TestCase):

    DUMMY_TODO_TITLE = 'Test Element'

    def setUp(self):
            self.todoList = TodoList()
            self.todoList.name = 'Test Todo List'
            self.todoList.save()

            self.todoListTestElement = Todo()
            self.todoListTestElement.title = self.DUMMY_TODO_TITLE
            self.todoListTestElement.due_date = datetime.today()
            self.todoListTestElement.favorite = False
            self.todoListTestElement.completed = True
            self.todoListTestElement.list = self.todoList
            self.todoListTestElement.save()

    def test_create_todo(self):

        # Voir combien sont present dans notre DB (Todos)
        # Ajouter un objet dans notre DB
        # Valider que le nombre d'objets dans notre DB a ete incremente de 1

        nbr_of_todo_before_add = Todo.objects.count()

        new_todo = Todo()
        new_todo.title = 'Acheter la banane'
        new_todo.due_date = datetime.today()
        new_todo.favorite = True
        new_todo.completed = False
        new_todo.list = self.todoList

        new_todo.save()

        nbr_of_todo_after_add = Todo.objects.count()

        self.assertTrue(nbr_of_todo_after_add == nbr_of_todo_before_add + 1)


    def test_update_todo(self):

        self.assertEqual(self.todoListTestElement.title, self.DUMMY_TODO_TITLE)

        self.todoListTestElement.title = 'Change Todo Title'
        self.todoListTestElement.save()

        tempElement = Todo.objects.get(pk=self.todoListTestElement.pk)

        self.assertEqual(tempElement.title, 'Change Todo Title')


    def test_delete_todo(self):

        nbr_of_todos_before_delete = Todo.objects.count()

        self.todoListTestElement.delete()

        nbr_of_todos_after_delete = Todo.objects.count()

        self.assertTrue(nbr_of_todos_after_delete == nbr_of_todos_before_delete - 1)
