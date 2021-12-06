# Generated by Django 3.2.9 on 2021-11-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0006_users_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_username',
            field=models.CharField(default='', max_length=150, verbose_name='聊天用户名'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='chat_comment',
            field=models.CharField(max_length=1000, verbose_name='聊天内容'),
        ),
    ]
