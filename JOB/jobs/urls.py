"""Определяет схемы URL для jobs."""

from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех профессий.
    path('professions/', views.professions, name='professions'),
    # Страница с подробной информацией по отдельной профессии
    path('professions/<int:profession_id>/', views.profession, name='profession'),
    # Страница для добавления новой профессии
    path('new_profession/', views.new_profession, name='new_profession'),
    # Страница для добавления новой записи
    path('new_entry/<int:profession_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]