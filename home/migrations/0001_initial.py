# Generated by Django 4.1.2 on 2022-10-28 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField(blank=True, max_length=500)),
                ('view_Time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
