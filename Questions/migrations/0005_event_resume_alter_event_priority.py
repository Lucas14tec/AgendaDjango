# Generated by Django 4.0.2 on 2022-02-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0004_rename_author_event_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='resume',
            field=models.CharField(default=1, max_length=1000, verbose_name='Descrição do Evento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='priority',
            field=models.CharField(choices=[('0', 'Sem Problemas'), ('1', 'Normal'), ('2', 'Urgente'), ('3', 'Muito Urgente')], max_length=1, verbose_name='Prioridade'),
        ),
    ]
