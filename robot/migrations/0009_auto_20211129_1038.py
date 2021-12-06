# Generated by Django 3.2.9 on 2021-11-29 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0008_auto_20211129_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='carbohydrate',
            field=models.IntegerField(default=0, verbose_name='碳水化合物'),
        ),
        migrations.AddField(
            model_name='users',
            name='fat',
            field=models.IntegerField(default=0, verbose_name='脂肪'),
        ),
        migrations.AddField(
            model_name='users',
            name='protein',
            field=models.IntegerField(default=0, verbose_name='蛋白质'),
        ),
    ]
