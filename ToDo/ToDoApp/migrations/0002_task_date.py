# Generated by Django 4.2 on 2023-05-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-04-12'),
            preserve_default=False,
        ),
    ]