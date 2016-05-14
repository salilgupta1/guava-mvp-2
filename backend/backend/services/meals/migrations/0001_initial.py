# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.CharField(blank=True, max_length=25)),
                ('unit_measurement', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField(blank=True)),
                ('cook_time', models.CharField(blank=True, max_length=25)),
                ('serving_portion', models.CharField(blank=True, max_length=50)),
                ('original_source', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('direction', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Recipe'),
        ),
    ]