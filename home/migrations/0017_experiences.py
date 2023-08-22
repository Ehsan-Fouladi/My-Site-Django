# Generated by Django 4.2.2 on 2023-08-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_planprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_days', models.CharField(max_length=50, verbose_name='تاریخ')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('subjects', models.TextField(verbose_name='موضوع')),
            ],
            options={
                'verbose_name': 'تجربه',
                'verbose_name_plural': 'تجربیات',
            },
        ),
    ]