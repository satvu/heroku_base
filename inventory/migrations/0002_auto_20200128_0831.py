# Generated by Django 3.0.2 on 2020-01-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='when',
            field=models.DateField(),
        ),
    ]
