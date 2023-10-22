from django.db import models


class Task(models.Model):
    title = models.CharField('Название статьи', max_length=50)
    task = models.TextField('Статья')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Статья'