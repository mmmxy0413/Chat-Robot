# Generated by Django 3.2.9 on 2021-11-29 10:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0010_auto_20211129_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_username', models.CharField(default='', max_length=150, verbose_name='用户名')),
                ('info_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('calorie', models.FloatField(default=0, verbose_name='卡路里')),
                ('carbohydrate', models.FloatField(default=0, verbose_name='碳水化合物')),
                ('fat', models.FloatField(default=0, verbose_name='脂肪')),
                ('protein', models.FloatField(default=0, verbose_name='蛋白质')),
            ],
            options={
                'verbose_name': '饮食信息',
                'verbose_name_plural': '饮食信息',
            },
        ),
    ]
