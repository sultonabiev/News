from django.db import models
from django.utils import timezone

class MyImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='my_image_uploads/')

class Task(models.Model):
    title = models.CharField('Название статьи', max_length=50)
    task = models.TextField('Статья')
    CATEGORY_CHOICES = (
        ('спорт', 'Спорт'),
        ('Политика', 'Политика'),
        ('группа 44', 'Группа 44'),
        ('не важные новости', 'Не Важные Новости'))
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image = models.ForeignKey(MyImage, on_delete=models.SET_NULL, blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Статьи'
