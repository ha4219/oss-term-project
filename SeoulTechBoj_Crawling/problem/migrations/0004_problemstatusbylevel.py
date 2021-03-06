# Generated by Django 3.0 on 2021-09-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0003_solvedproblem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemStatusByLevel',
            fields=[
                ('level', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('total', models.IntegerField()),
                ('solved', models.IntegerField()),
                ('notSolved', models.IntegerField()),
            ],
        ),
    ]
