# Generated by Django 3.1.2 on 2021-06-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDePrueba', '0002_auto_20210602_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut_cliente',
            field=models.IntegerField(help_text='Llave primaria Cliente', primary_key=True, serialize=False),
        ),
    ]
