from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),  # Home page URL
  path("todos/", views.todos, name="Todos"),  # Todos page URL
]