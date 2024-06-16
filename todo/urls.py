from django.contrib import admin
from django.urls import path
from todo.views import DeleteTodo, EditTodo, TodoAppView, AddTodo, UpdateTodoItem

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoAppView, name="todolist"),
    path("todo/", AddTodo, name="addTodo"),
    path("todo/<int:item_id>/delete/", DeleteTodo, name="deleteTodo"),
    path("todo/<int:item_id>/edit/", EditTodo, name="editTodo"),
    path("todo/<int:item_id>/update/", UpdateTodoItem, name="updateTodo"),
]