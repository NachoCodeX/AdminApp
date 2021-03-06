# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('PYC', 'Perfumería y cosméticos'), ('RYH', 'Ropa y del hogar')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Campaing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('campaing_num', models.PositiveIntegerField(default=0)),
                ('deperture_date', models.DateField()),
                ('arrival_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.AddField(
            model_name='article',
            name='campaing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avon.Campaing'),
        ),
    ]
