# Generated by Django 2.0.3 on 2018-03-14 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0006_auto_20180314_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
    ]
