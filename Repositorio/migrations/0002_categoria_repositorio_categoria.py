# Generated by Django 4.0.6 on 2022-08-02 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Repositorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoria', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='repositorio',
            name='Categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Repositorio.categoria'),
            preserve_default=False,
        ),
    ]
