# Generated by Django 4.0.3 on 2022-03-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
