# Generated by Django 4.0 on 2022-10-30 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_user_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(default=True, max_length=100, null=True, verbose_name='موضوع'),
        ),
    ]