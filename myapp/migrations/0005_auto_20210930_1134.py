# Generated by Django 3.1.1 on 2021-09-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210930_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energy',
            name='enrgy10',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='energy',
            name='enrgy20',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='energy',
            name='enrgy30',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='energy',
            name='enrgy40',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='energy',
            name='enrgy50',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='energy',
            name='enrgy60',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]