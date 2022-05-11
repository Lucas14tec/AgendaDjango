# Generated by Django 4.0.1 on 2022-01-31 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Questions', '0002_rename_events_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event',
            field=models.CharField(max_length=80, verbose_name='Evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='priority',
            field=models.CharField(choices=[('0', 'Sem Problemas'), ('1', 'Normal'), ('2', 'Urgente'), ('3', 'Muito Urgente   ')], max_length=1, verbose_name='Prioridade'),
        ),
    ]
