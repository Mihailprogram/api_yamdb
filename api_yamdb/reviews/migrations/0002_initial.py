# Generated by Django 3.2 on 2023-03-28 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('titles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='titles.title', verbose_name='произведения'),
        ),
    ]