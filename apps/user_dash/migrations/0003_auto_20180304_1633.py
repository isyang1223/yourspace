# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-05 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dash', '0002_auto_20180304_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user_dash.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='received_msgs', to='user_dash.User'),
        ),
    ]
