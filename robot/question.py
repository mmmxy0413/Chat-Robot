import urllib, urllib.request, sys,json
import ssl

def getResponse(input):
    print('uu')
    print(input)
    host = 'https://znwd.market.alicloudapi.com'
    path = '/znwd'
    method = 'GET'
    appcode = 'e7a3eef9940c4e53a662eedefc7567e5'
    querys = 'content='+urllib.parse.quote(input)+'&product=znys&uuid=1234567890'
    bodys = {}
    url = host + path + '?' + querys

    request = urllib.request.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)
    content = json.loads(response.read().decode('utf-8'))
    print(content)
    response = content['msg']
    response = response.replace('此健康指导建议由智能小医提供，仅供参考，具体诊疗请一定要到医院在医生指导下进行！','')
    if len(response) > 200:
        response = response[:199]
    return response