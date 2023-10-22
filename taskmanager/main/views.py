from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
def about(request):
    return render(request, 'main/about.html')
def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма было неверной'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def profile(request):
    # Ваш код для страницы профиля
    context = {
        'user': request.user,  # Передача объекта пользователя в контекст
    }
    return render(request, 'main/profile.html', context)

