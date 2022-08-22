# Generated by Django 4.0.6 on 2022-08-02 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repositorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.TextField(max_length=50)),
                ('Descricao', models.TextField(max_length=3000)),
                ('Completo', models.BooleanField(default=False)),
            ],
        ),
    ]
