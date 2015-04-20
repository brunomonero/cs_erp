# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_function_pricelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricelist',
            name='name',
        ),
    ]
