# Generated by Django 3.1.2 on 2022-03-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]