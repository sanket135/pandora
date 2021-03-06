# Generated by Django 2.2.1 on 2021-02-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210225_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fruit',
            field=models.ManyToManyField(blank=True, to='api.Fruit'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api.Tag'),
        ),
        migrations.AlterField(
            model_name='user',
            name='vegetables',
            field=models.ManyToManyField(blank=True, to='api.Vegetable'),
        ),
    ]
