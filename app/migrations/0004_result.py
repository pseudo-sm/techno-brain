# Generated by Django 3.0.3 on 2020-02-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_question_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('score', models.CharField(max_length=100)),
            ],
        ),
    ]
