# Generated by Django 3.0.3 on 2020-02-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('a', models.CharField(max_length=100)),
                ('c', models.CharField(max_length=100)),
                ('d', models.CharField(max_length=100)),
                ('e', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
    ]
