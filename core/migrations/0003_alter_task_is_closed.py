# Generated by Django 4.2.4 on 2023-09-01 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_task_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_closed',
            field=models.BooleanField(default=True),
        ),
    ]
