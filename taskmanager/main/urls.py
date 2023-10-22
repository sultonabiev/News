from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('register', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='main/custom_login.html'), name='login'),
    path('news/category/<str:category>/', views.news_by_category, name='news_by_category'),
    path('task/<int:task_id>/', views.view_task, name='view_task'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/', views.task_list, name='task_list'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task/success/', views.success_page, name='success_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
