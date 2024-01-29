# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import apps.library.mixins
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('time_from', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('time_to', models.DateTimeField(db_index=True, default=None)),
                ('status', models.CharField(max_length=10, default='rented', choices=[('rented', 'rented'), ('returned', 'returned'), ('overdue', 'overdue')])),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Book')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.library.mixins.RentBookStatusMixin),
        ),
    ]
