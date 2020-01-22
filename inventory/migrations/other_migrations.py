from __future__ import unicode_literals
from django.db import migrations, models
from ./models import *

class Migration(migrations.Migration):

    initial = False

    dependencies = []

    operations = [        
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name="dish name")),
                ('price', models.IntegerField(verbose_name = 'price in pesos')),
                ('description', models.TextField(verbose_name = 'description of dish')),
                ('ingredients', models.ManyToManyField(Ingredient)),
                ('image', models.TextField(verbose_name='image url'))
            ],
        )
    ]