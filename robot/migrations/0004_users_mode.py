# Generated by Django 3.2.9 on 2021-11-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0003_auto_20211127_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='mode',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='模式'),
        ),
    ]
