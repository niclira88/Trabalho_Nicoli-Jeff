# Generated by Django 2.1 on 2018-08-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposed_law',
            name='resultado',
            field=models.BooleanField(default=True, verbose_name='resultado'),
        ),
    ]