# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-20 22:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True, max_length=180, null=True)),
                ('location', models.CharField(blank=True, max_length=180, null=True)),
                ('fee', models.FloatField(blank=True, null=True)),
                ('camera', models.CharField(blank=True, choices=[('DSLR', 'Digital Single Lens Reflex'), ('M', 'Mirrorless'), ('AC', 'Advanced Compact'), ('SLR', 'Single Lens Reflex')], max_length=180, null=True)),
                ('services', multiselectfield.db.fields.MultiSelectField(choices=[('weddings', 'Weddings'), ('headshots', 'HeadShots'), ('landscape', 'LandScape'), ('portraits', 'Portraits'), ('art', 'Art')], max_length=42)),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('photostyles', multiselectfield.db.fields.MultiSelectField(choices=[('blackandwhite', 'Black and White'), ('night', 'Night'), ('macro', 'Macro'), ('3d', '3D'), ('artistic', 'Artistic'), ('underwater', 'Underwater')], max_length=48)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
