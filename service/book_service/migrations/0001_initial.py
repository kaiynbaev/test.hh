# Generated by Django 4.2.7 on 2023-11-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Название')),
                ('author', models.CharField(max_length=70, verbose_name='Автор')),
                ('publication_year', models.IntegerField(verbose_name='Год издания')),
                ('ISBN', models.BigIntegerField(unique=True, verbose_name='ISBN')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
