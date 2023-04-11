from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('todo/<slug:slug>', views.details, name="todo"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('create', views.create, name="create"),




]
