# Generated by Django 3.2 on 2021-04-18 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_taskmodel_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='tag',
        ),
    ]