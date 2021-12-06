from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Users(AbstractUser):
    #nick_name = models.CharField(max_length=50, verbose_name='用户昵称', default='')
    gender = models.CharField(max_length=6, choices=(('male', 'male'), ('female', 'female')), default='female', verbose_name='性别')
    #address = models.CharField(max_length=100, default='', verbose_name='地址')
    #mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    captcha = models.CharField(max_length=100, default='', verbose_name='验证码') # 注册时输入的验证码
    mode = models.CharField(max_length=2, default='1',null=True, blank=True, verbose_name='模式')
    online = models.CharField(max_length=2, choices=(('0', '0'), ('1', '1')), default='0', verbose_name='在线')
    calorie = models.FloatField(default=0,verbose_name='卡路里')
    carbohydrate = models.FloatField(default=0,verbose_name='碳水化合物')
    fat = models.FloatField(default=0,verbose_name='脂肪')
    protein = models.FloatField(default=0,verbose_name='蛋白质')
    weight = models.FloatField(default=0,verbose_name='体重')
    height = models.FloatField(default=0,verbose_name='身高')
    age = models.IntegerField(default=0,verbose_name='年龄') 
    freqency = models.CharField(max_length=10, default='medium', verbose_name='频率')
    target = models.CharField(max_length=6, default='keep', verbose_name='目标')


    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Chat(models.Model):
    chat_comment = models.CharField(max_length=1000, verbose_name="聊天内容")
    send_time = models.DateTimeField(default=timezone.now, verbose_name="发送时间")
    chat_username = models.CharField(max_length=150,verbose_name='聊天用户名',default='')

    class Meta:
        verbose_name = '聊天记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chat_comment

class UsersInfo(models.Model):
    info_username = models.CharField(max_length=150,verbose_name='用户名',default='')
    info_time = models.CharField(max_length=150, verbose_name="时间")
    calorie = models.FloatField(default=0,verbose_name='卡路里')
    carbohydrate = models.FloatField(default=0,verbose_name='碳水化合物')
    fat = models.FloatField(default=0,verbose_name='脂肪')
    protein = models.FloatField(default=0,verbose_name='蛋白质')

    class Meta:
        verbose_name = '饮食信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.info_username
# """
# 创建学生信息表模型
# """
# from django.db import models

# """
#  该类是用来生成数据库的 必须要继承models.Model
# """
# class Users(models.Model):
#     """
#     创建如下几个表的字段
#     """
#     # 学号 primary_key=True: 该字段为主键
#     studentNum = models.CharField('学号', primary_key=True, max_length=15)
#     # 姓名 字符串 最大长度20
#     name = models.CharField('姓名', max_length=20)
#     # 年龄 整数 null=False, 表示该字段不能为空
#     age = models.IntegerField('年龄', null=False)
#     # 性别 布尔类型 默认True: 男生 False:女生
#     sex = models.BooleanField('性别', default=True)
#     # 手机 unique=True 该字段唯一
#     mobile = models.CharField('手机', unique=True, max_length=15)
#     # 创建时间 auto_now_add：只有在新增的时候才会生效
#     createTime = models.DateTimeField(auto_now_add=True)
#     # 修改时间 auto_now： 添加和修改都会改变时间
#     modifyTime = models.DateTimeField(auto_now=True)

#     # 指定表名 不指定默认APP名字——类名(app_demo_Student)
#     class Meta:
#         db_table = 'student'


# """
# 学生社团信息表
# """
# class Chat(models.Model):
#     # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
#     id = models.IntegerField(primary_key=True)
#     # 社团名称
#     unionName = models.CharField('社团名称', max_length=20)
#     # 社团人数
#     unionNum = models.IntegerField('人数', default=0)
#     # 社团负责人 关联Student的主键 即studentNum学号 一对一的关系,on__delete 属性在django2.0之后为必填属性后面会介绍
#     unionRoot = models.OneToOneField(Users, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'student_union'


# """
# OneToOneField： 一对一
# ForeignKey: 一对多
# ManyToManyField： 多对多(没有ondelete 属性)
# """
