# Generated by Django 3.0.3 on 2020-02-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200225_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='set',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
