# Generated by Django 5.0.4 on 2024-05-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeekFoodsApp', '0002_alter_ingredient_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userweekfoods',
            old_name='recipe',
            new_name='recipes',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.FloatField(blank='False', null='False', verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(blank='False', null='False', verbose_name='calorias'),
        ),
    ]
