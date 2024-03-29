# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-08 08:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='user',
        ),
        migrations.RemoveField(
            model_name='recyclingrequest',
            name='user',
        ),
        migrations.AlterField(
            model_name='mobileuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mobile_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recyclingrequest',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver_requests', to='collector.Receiver', verbose_name='دریافت کننده'),
        ),
        migrations.AlterField(
            model_name='recyclingrequest',
            name='requester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_requests', to='collector.MobileUser', verbose_name='درخواست دهنده'),
        ),
    ]
