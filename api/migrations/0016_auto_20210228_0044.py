# Generated by Django 2.2.1 on 2021-02-28 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210227_0207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ManyToManyField(blank=True, null=True, to='api.Company'),
        ),
    ]
