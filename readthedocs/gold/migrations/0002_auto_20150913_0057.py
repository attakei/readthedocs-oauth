# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golduser',
            name='level',
            field=models.CharField(default=b'v1-org-5', max_length=20, verbose_name='Level', choices=[(b'v1-org-5', b'$5/mo'), (b'v1-org-10', b'$10/mo'), (b'v1-org-15', b'$15/mo'), (b'v1-org-20', b'$20/mo'), (b'v1-org-50', b'$50/mo'), (b'v1-org-100', b'$100/mo')]),
        ),
    ]