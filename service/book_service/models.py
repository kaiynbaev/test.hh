from django.db import models
# Create your models here.


class book(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Название'
    )
    author = models.CharField(
        max_length=70,
        verbose_name='Автор'
    )
    publication_year = models.IntegerField(
        verbose_name='Год издания',
    )
    ISBN = models.BigIntegerField(
        unique=True,
        verbose_name='ISBN'
    )
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
    
    def __str__(self) -> str:
        return self.name