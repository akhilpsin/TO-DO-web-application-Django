# Generated by Django 3.2.3 on 2021-06-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-04-23'),
            preserve_default=False,
        ),
    ]
