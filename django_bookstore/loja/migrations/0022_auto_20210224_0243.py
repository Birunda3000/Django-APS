# Generated by Django 3.1.5 on 2021-02-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0021_compra_avaliado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='valor',
            field=models.FloatField(default=0.0),
        ),
    ]
