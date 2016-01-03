# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-02 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text=b'Name of project (just for reminding purpose).', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='path',
            field=models.CharField(help_text=b'Absolute path on server to clone repo into.', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo',
            field=models.CharField(help_text=b'SSH URL of the repository (eg. git@git.bizidea.co.th:Bizidea/bizidea-mailer.git)', max_length=255),
        ),
    ]
