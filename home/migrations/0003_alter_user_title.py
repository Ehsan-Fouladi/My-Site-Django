# Generated by Django 4.0 on 2022-10-30 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_user_body_alter_user_email_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(max_length=100, verbose_name='موضوع'),
        ),
    ]