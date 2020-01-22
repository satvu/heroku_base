from __future__ import unicode_literals
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = False

    dependencies = []

    operations = [        
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.TimeField(auto_now_add=True, verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, auto_created=True, verbose_name=b'ingredient name')),
                ('amount', models.IntegerField(auto_created=True))
            ]
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name="dish name")),
                ('price', models.IntegerField(verbose_name = 'price in pesos')),
                ('description', models.TextField(verbose_name = 'description of dish')),
                ('image', models.TextField(verbose_name='image url'))
            ],
        )
    ]