# Generated by Django 5.0.2 on 2024-10-23 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('class_name', models.CharField(max_length=50)),
                ('roll_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('staff', 'Office Staff'), ('librarian', 'Librarian')], max_length=10),
        ),
        migrations.CreateModel(
            name='LibraryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateField()),
                ('return_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
        ),
        migrations.CreateModel(
            name='FeesHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('remarks', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
        ),
    ]
