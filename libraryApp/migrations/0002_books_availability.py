# Generated by Django 3.2.5 on 2022-04-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='availability',
            field=models.IntegerField(default=1),
        ),
    ]
