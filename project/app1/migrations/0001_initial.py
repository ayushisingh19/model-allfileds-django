# Generated by Django 5.0.7 on 2024-07-19 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
                ('dep_discription', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=50, null=True)),
                ('stu_contact', models.IntegerField()),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
            ],
        ),
    ]