# Generated by Django 2.0.3 on 2018-03-13 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_auto_20180313_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
        migrations.AlterField(
            model_name='rasgos',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
    ]
