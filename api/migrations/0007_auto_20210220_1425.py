# Generated by Django 2.2.1 on 2021-02-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210220_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registered',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]