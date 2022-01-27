# Generated by Django 2.2.5 on 2022-01-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('topic', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=500)),
                ('professor_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'lecture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=120)),
                ('company', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=800)),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'professor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('company_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=150)),
                ('job_fields', models.CharField(max_length=200)),
                ('required_career', models.CharField(max_length=200)),
                ('required_education', models.CharField(max_length=100)),
                ('employment_type', models.CharField(max_length=50)),
                ('work_place', models.CharField(max_length=200)),
                ('deadlines', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'recruit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diaryapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='%Y/%m/%d')),
                ('diary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diaryapp.Diary')),
            ],
        ),
    ]
