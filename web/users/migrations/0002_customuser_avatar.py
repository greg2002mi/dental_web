# Generated by Django 4.2.5 on 2023-09-22 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='noface.png', upload_to='profile_images/'),
        ),
    ]