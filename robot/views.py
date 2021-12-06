from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
import requests
import json
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from robot.models import Chat, Users,UsersInfo
from robot.forms import LoginForm, RegisterForm, registerForm,ModeForm
from django.contrib.auth import login, logout
# 验证码需要导入的模块
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from robot.ChatInterface import *
from robot.recipe.main import *
from robot.question import getResponse
from robot.data_pro import getMaterial,getInfo
from robot.crawler import search_web
from robot.Nutrition import nutrient

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 创建验证码
def captcha():
    # 验证码，第一次请求
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha
 

def jarge_captcha(captchaStr, captchaHashkey):
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey) 
            # 如果验证码匹配
            if get_captcha.response == captchaStr.lower():  
                return True
        except:
            return False
    else:
        return False

def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')

def get_response(info):
    #调用智能问答API
    response = ''
    if getMode() == '1':
        response = chatting_interface(info)
    if getMode() == '2':
        #爬虫结果
        recipe = search_web(info)
        crawler_info = ''
        if len(recipe.keys()) == 4:
            crawler_info = '卡路里为'+recipe['calorie']+'大卡,碳水化合物为'+recipe['carbohydrate']+'g,脂肪为'+recipe['fat']+'g,蛋白质为'+recipe['protein']+'g。'
        if len(recipe.keys()) == 5:
            ingredient_list = recipe['ingredient']
            crawler_info += '原料为:'
            for j in range(len(ingredient_list)-1):
                crawler_info += ingredient_list[j]
                crawler_info += ','
            crawler_info += ingredient_list[len(ingredient_list)-1]
            crawler_info += '。卡路里为'+recipe['calorie']+'大卡,碳水化合物为'+recipe['carbohydrate']+'g,脂肪为'+recipe['fat']+'g,蛋白质为'+recipe['protein']+'g。'
        response += crawler_info
        #阿里结果
        ali_info = getResponse(info)
        error_code1 = '抱歉，小ｉ没能理解您的问题'
        error_code2 = '抱歉，小ｉ暂时无法提供满意答案，建议您咨询在线医生。'
        if ali_info == error_code1 or ali_info == error_code2:
            ali_info = ''
        response += ali_info
    #material_name = getMaterial(info)
    #information = getInfo(info)
    # if material_name:
    #     response = getResponse(material_name)
    # else:
    #     print('haha')
    #     response = getResponse(info)
    #爬虫结果
    # crawler_info = search_web(info)
    # #阿里结果
    # ali_info = getResponse(info)
    
    # #普通对话结果
    # chat_info = chatting_interface(info)
    
    # if information:
    #     response += information
    # else:
    #     response += ''
    return response


class Index(View):
    def get(self, request):
        # print('app robot 中的 index视图')
        # raise ValueError("呵呵")
        # return HttpResponse("O98K")
        if request.user.username == '':
            # print(request.user.username+"#######")
            return render(request, 'login.html', {})
        return render(request, 'index.html', {'mode':getMode()})

    def render(self):
        print("in index/render")
        return HttpResponse("O98K")

    def post(self, request):
        comment = request.POST.get('comment', '')
        recevie = get_response(comment)
        users = Users.objects.get(online='1')
        chat1 = Chat(chat_comment=comment,chat_username = users.username)
        chat2 = Chat(chat_comment=recevie,chat_username = users.username)
        chat1.save()
        chat2.save()
        return render(request, 'index.html', {'comment': comment, 'recevie': recevie,'mode':getMode()})


def record(request):
    if request.user.username == '':
        # print(request.user.username+"#######")
        return render(request, 'login.html', {})
    #all_chats = Chat.objects.all()
    users = Users.objects.get(online='1')
    all_chats = Chat.objects.filter(chat_username=users.username)
    return render(request, 'record.html', {'all_chats': all_chats})


def check(username=None, password=None):
    try:
        user = Users.objects.get(Q(username=username) | Q(email=username))
        if user.check_password(password):
            return user
    except Exception as e:
        return None

def setOnline(username):
    Users.objects.filter(Q(username=username) | Q(email=username)).update(online='1')

def offline():
    Users.objects.update(online='0')

class Login(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = check(username=username, password=password)
            if user is not None:
                login(request, user)
                setOnline(username)
                return render(request, 'index.html', {'mode':getMode()})
            else:
                return render(request, 'login.html', {'msg': "用户不存在或密码错误"})
        else:
            return render(request, 'login.html', {'login_form': login_form})

def logoutView(request):
    logout(request)
    offline()
    return render(request, 'login.html', {})

def createUserInfo(username):
    UsersInfo.objects.create(info_username = username)

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form, 'captcha': captcha})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            if Users.objects.filter(email=data['email']):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已存在', 'captcha': captcha})
            if Users.objects.filter(username=data['username']):
                return render(request, 'register.html', {'msg': '此用户名已被使用', 'captcha': captcha})
            captchaHashkey = request.POST.get('hashkey', '')
            if jarge_captcha(data['captcha'], captchaHashkey):
                register_form.cleaned_data['password'] = make_password(register_form.cleaned_data['password'])
                Users.objects.create(**register_form.cleaned_data)
                #createUserInfo(data['username'])
                return render(request, 'info.html', {'username':data['username'],'msg': "注册成功,请填写基础健康信息..."})
            else:
                return render(request, 'register.html', {'msg': "验证码错误"})
        else:
            return render(request, 'register.html', {'register_form': register_form, 'captcha': captcha})
def test(request):
    return render(request, 'info.html')
def info_finish(request):
    username = request.POST.get("username")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    height = request.POST.get("height")
    weight = request.POST.get("weight")
    target = request.POST.get("target")
    freqency = request.POST.get("freqency")

    Users.objects.filter(username=username).update(gender=gender)
    Users.objects.filter(username=username).update(age=age)
    Users.objects.filter(username=username).update(height=height)
    Users.objects.filter(username=username).update(weight=weight)
    Users.objects.filter(username=username).update(target=target)
    Users.objects.filter(username=username).update(freqency=freqency)

    return render(request, 'login.html', {'msg': "注册成功,请登录..."})


def upload(request):
    if request.method == 'POST':# 获取对象
        obj = request.FILES.get('fafafa')
        picture = os.path.join(BASE_DIR, 'media', obj.name)
        res = {
            "url": "media/"+str(obj.name)   # 路径
        }
        recevie = ''
        f = open(os.path.join(BASE_DIR, 'media', obj.name), 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        food_name = recipe_recognitino(picture)
        recevie += food_name
        recevie += '。'
        recipe = search_web(food_name)
        ingredient_list = recipe['ingredient']
        ingredient_str = "".join(ingredient_list)
        crawler_info = ''
        crawler_info += '原料为:'
        for j in range(len(ingredient_list)-1):
            crawler_info += ingredient_list[j]
            crawler_info += ','
        crawler_info += ingredient_list[len(ingredient_list)-1]
        crawler_info += '。卡路里为'+recipe['calorie']+'大卡,碳水化合物为'+recipe['carbohydrate']+'g,脂肪为'+recipe['fat']+'g,蛋白质为'+recipe['protein']+'g。'
        recevie += crawler_info
        #将四项指标与时间存储
        import datetime
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        info_time = str(year) + '-'+ str(month) + '-'+ str(day)
        users1 = Users.objects.get(online='1')
        username = users1.username
        #users = UsersInfo.objects.get(info_username=username)
        UsersInfo.objects.create(info_username = username,info_time = info_time,calorie=recipe['calorie'],carbohydrate=recipe['carbohydrate'],fat=recipe['fat'],protein=recipe['protein'])

        #阿里结果
        ali_info = getResponse(ingredient_str)
        error_code1 = '抱歉，小ｉ没能理解您的问题'
        error_code2 = '抱歉，小ｉ暂时无法提供满意答案，建议您咨询在线医生。'
        if ali_info == error_code1 or ali_info == error_code2:
            ali_info = ''
        recevie += ali_info
        #material_name = getMaterial(food_name)
        # if material_name:
        #     recevie = getResponse(material_name)
        #     information = getInfo(material_name)
        #     if information:
        #         recevie += str(information)
        #     else:
        #         recevie += ''
        #     print(recevie)
        # else:
        #     recevie += food_name +'。'
        #     recevie += chatting_interface(food_name)
    return render(request, 'index.html',{'pic_path':res, 'recevie':recevie,'mode':getMode()})

def mode1(request):
    users = Users.objects.get(online='1')
    Users.objects.filter(Q(username=users.username) | Q(email=users.username)).update(mode='1')
    return render(request, 'index.html',{'mode':'1'})

def mode2(request):
    users = Users.objects.get(online='1')
    Users.objects.filter(Q(username=users.username) | Q(email=users.username)).update(mode='2')
    return render(request, 'index.html',{'mode':'2'})

def getMode():
    users = Users.objects.get(online='1')
    return users.mode

def getNeed():
    users = Users.objects.get(online='1')
    username = users.username
    import datetime
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    info_time = str(year) + '-'+ str(month) + '-'+ str(day)
    all_nutritions = UsersInfo.objects.filter(Q(info_username=users.username) & Q(info_time=info_time))
    calorie = 0.0
    carbohydrate = 0.0
    protein = 0.0
    fat = 0.0
    for nutrition in all_nutritions:
        calorie += nutrition.calorie
        carbohydrate += nutrition.carbohydrate
        fat += nutrition.fat
        protein += nutrition.protein
    weight = users.weight
    height = users.height
    age = users.age
    freqency = users.freqency
    gender = users.gender
    target = users.target

    all_need = nutrient(weight,height,age,freqency,gender,target)
    dict = {}
    dict['calorie'] = round(all_need['total']['calorie'] - calorie,2)
    dict['carbohydrate'] = round(all_need['total']['carbohydrate'] - carbohydrate,2)
    dict['fat'] = round(all_need['total']['fat'] - fat,2)
    dict['protein'] = round(all_need['total']['protein'] - protein,2)
    return dict

def chart(request):
    users = Users.objects.get(online='1')
    username = users.username;
    res = {
        "username": users.username,
        "age" : users.age,
        "height":users.height,
        "weight":users.weight
    }
    all_infos = UsersInfo.objects.filter(info_username=users.username)
    dict = getNeed()
    need_info = '您今日仍需摄入,卡路里:' + str(dict['calorie'])+'大卡,碳水化合物:'+ str(dict['carbohydrate'])+'g,脂肪:'+str(dict['fat'])+'g,蛋白质'+str(dict['protein'])+'g。'
    return render(request, 'chart.html', {'res':res,'all_infos':all_infos,'need_info':need_info})
    