# Generated by Django 4.0.3 on 2022-03-11 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]
