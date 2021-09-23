# Generated by Django 3.0 on 2021-09-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problemId', models.IntegerField(primary_key=True, serialize=False)),
                ('titleKo', models.CharField(max_length=200)),
                ('isSolvable', models.BooleanField()),
                ('acceptedUserCount', models.IntegerField()),
                ('level', models.IntegerField()),
                ('averageTries', models.DecimalField(decimal_places=5, max_digits=10)),
                ('solved', models.BooleanField(default=False)),
                ('tag', models.ManyToManyField(to='tag.Tag')),
            ],
        ),
    ]
