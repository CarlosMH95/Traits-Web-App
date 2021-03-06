# Generated by Django 2.0.3 on 2018-03-07 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='')),
                ('confirmado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('direccion', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_actualizado', models.DateField(auto_now=True)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='rasgos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('POSI', 'Positivo'), ('NEGA', 'Negativo'), ('NEUT', 'Neutral')], max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='comentarios',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.persona'),
        ),
    ]
