# Generated by Django 3.2.5 on 2022-04-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0002_books_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_users',
            name='password',
            field=models.CharField(max_length=120),
        ),
    ]
