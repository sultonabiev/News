from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import ImageUploadForm
from .models import MyImage

def index(request):
    tasks = Task.objects.all()
    search_query = request.GET.get('search_pr')

    if search_query:
        tasks = Task.objects.filter(title__icontains=search_query)

    context = {'title': 'Главная страница сайта', 'tasks': tasks}
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

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
    context = {'user': request.user}
    return render(request, 'main/profile.html', context)

def news_by_category(request, category):
    tasks = Task.objects.filter(category=category)
    context = {'category': category, 'tasks': tasks}
    return render(request, 'main/news_by_category.html', context)

def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'main/task_detail.html', {'task': task})

def create_task(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_task', task_id=form.instance.id)
    else:
        form = ArticleForm()
    return render(request, 'main/create_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_task', task_id=task.id)
    else:
        form = ArticleForm(instance=task)
    return render(request, 'main/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('home')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'main/task_list.html', {'tasks': tasks})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            task_id = request.POST.get('task_id')
            if task_id:
                task = Task.objects.get(pk=task_id)
                task.image = image
                task.save()
            return redirect('success_page')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')