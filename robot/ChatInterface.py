import json
import urllib.request

def chatting_interface(text_input):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"

    req = {
        "perception":
        {
            "inputText":
            {
                "text": text_input
            },

            "selfInfo":
            {
                "location":
                {
                    "city": "北京",
                    "province": "北京",
                    "street": "中关村大街"
                }
            }
        },

        "userInfo": 
        {
            "apiKey": "9044313b82154929bd1c923975d96a1e",
            "userId": "OnlyUseAlphabet"
        }
    }
    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    print('Turing的回答：')
    print('code：' + str(intent_code))
    print('text：' + results_text)
    return results_text

# text_input=input("我：")
# chatting_interface(text_input)