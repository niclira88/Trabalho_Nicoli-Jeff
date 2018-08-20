# Generated by Django 2.1 on 2018-08-20 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0002_proposed_law_resultado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proposed', models.IntegerField(default=0, verbose_name='id_proposed')),
                ('id_user', models.IntegerField(default=0, verbose_name='id_user')),
                ('comment', models.TextField(verbose_name='Comentario')),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
            },
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proposed', models.IntegerField(default=0, verbose_name='id_proposed')),
                ('id_user', models.IntegerField(default=0, verbose_name='id_user')),
                ('votocontra', models.IntegerField(default=0, verbose_name='votos contra')),
                ('votoafavor', models.IntegerField(default=0, verbose_name='votos a favor')),
            ],
            options={
                'verbose_name': 'voto',
                'verbose_name_plural': 'votos',
            },
        ),
        migrations.AddField(
            model_name='proposed_law',
            name='active',
            field=models.BooleanField(default=True, verbose_name='ativado'),
        ),
        migrations.AddField(
            model_name='proposed_law',
            name='final_time',
            field=models.TimeField(default=datetime.datetime(2018, 8, 20, 12, 16, 42, 182224), verbose_name='horario final'),
        ),
    ]
