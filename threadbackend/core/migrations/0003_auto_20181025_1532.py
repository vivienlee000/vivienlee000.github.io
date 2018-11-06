# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-25 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181025_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateField(verbose_name='date published')),
                ('issu', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='static/imgs/issues', verbose_name='Cover (best ratio is 3:2)')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='static/imgs/articles', verbose_name='Cover (best ratio is 3:2)'),
        ),
    ]