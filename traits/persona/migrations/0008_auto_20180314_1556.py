# Generated by Django 2.0.3 on 2018-03-14 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_auto_20180314_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rasgos',
            name='persona',
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
    ]
