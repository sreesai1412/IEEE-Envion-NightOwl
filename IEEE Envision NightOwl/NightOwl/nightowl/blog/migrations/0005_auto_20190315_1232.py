# Generated by Django 2.1.5 on 2019-03-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190314_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='nc1products',
            name='currently_present',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nc2products',
            name='currently_present',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nc3products',
            name='currently_present',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]