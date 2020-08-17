from django.db import models

class Post(models.Model):
    name = models.CharField(verbose_name='Заголовок: ', max_length=200)
    slug = models.SlugField(unique=True)
    img = models.ImageField(verbose_name='Зображення: ', upload_to='static/img/posts/')
    fdesc = models.TextField(verbose_name='Коротке описання', max_length=500)
    sdesc = models.TextField(verbose_name='Повний опис')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
