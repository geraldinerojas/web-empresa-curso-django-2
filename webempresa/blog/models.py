from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Nombre de la categoría')
    created = models.DateField(auto_now_add=True,
                               verbose_name='Fecha de creación')
    updated = models.DateField(auto_now=True,
                               verbose_name='Última modificación')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='blog/',
                              null=True, blank=True)
    published = models.DateField(verbose_name='Fecha de publicación',
                                 default=now)
    author = models.ForeignKey(User, verbose_name='Autor',
                               on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name="get_posts")
    created = models.DateField(auto_now_add=True,
                               verbose_name='Fecha de creación')
    updated = models.DateField(auto_now=True,
                               verbose_name='Última modificación')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']

    def __str__(self):
        return self.title
