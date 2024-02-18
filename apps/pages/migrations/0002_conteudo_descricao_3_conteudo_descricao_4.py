# Generated by Django 4.2.9 on 2024-02-13 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conteudo',
            name='descricao_3',
            field=models.CharField(blank=True, help_text='Descrição mais curta até 200 caracteres', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='conteudo',
            name='descricao_4',
            field=models.TextField(blank=True, help_text='Descrição mais longa', null=True),
        ),
    ]
