# Generated by Django 2.1 on 2018-12-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='claimed_user',
            field=models.TextField(null=True),
        ),
    ]
