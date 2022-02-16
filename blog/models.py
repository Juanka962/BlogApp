from django.db import models


class Post(models.Model):
    title = models.CharField(
        'Titulo',
        max_length=200
    )
    author = models.ForeignKey(
        'auth.User',
        verbose_name='Autor',
        on_delete=models.CASCADE,
    )
    body = models.TextField(
        'Cuerpo'
    )
    def __str__(self):
        return self.title
