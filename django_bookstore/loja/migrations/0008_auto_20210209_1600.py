# Generated by Django 3.1.5 on 2021-02-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_auto_20210209_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='loja.Livro'),
        ),
    ]