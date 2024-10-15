# Generated by Django 5.0.4 on 2024-06-04 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MenuSemanal', '0001_initial'),
        ('WeekFoodsApp', '0007_alter_recipe_ingredients_alter_userweekfoods_recipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklymenu',
            name='recipe_sug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WeekFoodsApp.recipe', verbose_name='Receta del menú semanal'),
        ),
        migrations.AlterField(
            model_name='weeklymenu',
            name='user_active',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WeekFoodsApp.userweekfoods', verbose_name='Nombre de usuario'),
        ),
    ]
