# Generated by Django 3.0.3 on 2020-02-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='score2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]