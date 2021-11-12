# Generated by Django 3.2.9 on 2021-11-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0002_rename_guitars_guitar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='frets',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='no_strings',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True),
        ),
    ]
