from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profession, Entry
from .forms import ProfessionForm, EntryForm

# Create your views here.


def index(request):
    """Домашняя страница приложения Job"""
    return render(request, 'jobs/index.html')


@login_required
def professions(request):
    """Выводит список профессий."""
    professions = Profession.objects.order_by('date_added')
    context = {'professions': professions}
    return render(request, 'jobs/professions.html', context)


@login_required
def profession(request, profession_id):
    """Выводит одну профессию и все ее записи."""

    profession = Profession.objects.get(id=profession_id)
    entries = profession.entry_set.order_by('-date_added')
    context = {'profession': profession, 'entries': entries}
    return render(request, 'jobs/profession.html', context)


@login_required
def new_profession(request):
    """Опредиляет новую профессию"""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = ProfessionForm
    else:
        # Отправлены данные POST; обработать данные.
        form = ProfessionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:professions')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'jobs/new_profession.html', context)


@login_required
def new_entry(request, profession_id):
    """Добавляет новую запись по конкретной профессии."""
    profession = Profession.objects.get(id=profession_id)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.profession = profession
            new_entry.save()
            return redirect('jobs:profession', profession_id=profession_id)

    # Вывести пустую или недействительную форму.
    context = {'profession': profession, 'form': form}
    return render(request, 'jobs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    profession = entry.profession
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:profession', profession_id=profession.id)
    context = {'entry': entry, 'profession': profession, 'form': form}
    return render(request, 'jobs/edit_entry.html', context)