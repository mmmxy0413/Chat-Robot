"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.urls import include
from robot.views import *
from .settings import STATIC_ROOT
from .settings import MEDIA_ROOT,MEDIA_URL

from django.conf.urls.static import static
from . import settings
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    url('captcha', include("captcha.urls")),
    path('refresh_captcha/', refresh_captcha),    # 刷新验证码，ajax
    path('', Index.as_view(), name="index"),
    path('record', record, name="search"),
    path('login', Login.as_view(), name="login"),
    path('logout', logoutView, name="logout"),
    path('register', RegisterView.as_view(), name='register'),
    path('upload',upload, name='upload'),
    path('mode1',mode1,name='mode1'),
    path('mode2',mode2,name='mode2'),
    path('chart',chart,name='chart'),
    path('info_finish',info_finish,name='info_finish'),
    path('test',test,name='test'),
    path(r'media/(?P<path>.*)', serve,{'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]+static(MEDIA_URL, document_root=MEDIA_ROOT)

# from django.conf import settings

# if settings.DEBUG:
#     from django.conf.urls.static import static

#     urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
#     )