# Generated by Django 2.0.3 on 2018-03-13 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0004_auto_20180313_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
    ]