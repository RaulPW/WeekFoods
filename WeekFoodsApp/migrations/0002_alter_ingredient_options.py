# Generated by Django 5.0.4 on 2024-05-07 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeekFoodsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name_ingredient']},
        ),
    ]
