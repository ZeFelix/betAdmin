# Generated by Django 2.2.1 on 2019-06-27 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_squashed_0002_auto_20190627_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
