# Generated by Django 4.2.5 on 2023-09-22 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dental', '0003_faq_is_read_faq_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='more', to=settings.AUTH_USER_MODEL),
        ),
    ]
