# Generated by Django 2.2.5 on 2022-01-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Til',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('content', models.CharField(max_length=700, null=True)),
                ('img', models.CharField(blank=True, max_length=700, null=True)),
            ],
            options={
                'db_table': 'til',
                'managed': False,
            },
        ),
    ]
