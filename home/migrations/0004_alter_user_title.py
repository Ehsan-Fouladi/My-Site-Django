# Generated by Django 4.0 on 2022-10-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_user_body_alter_user_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
