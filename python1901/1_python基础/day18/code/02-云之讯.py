
# 云之讯
# PEP8代码规范

import requests
import random


def send_sms(phone, vcode):
    '''
    发送短信
    :param phone: 手机号
    :param vcode: 验证码
    :return: 发送的结果
    '''
    # YZX_SMS_URL
    url = 'https://open.ucpaas.com/ol/sms/sendsms'

    param = {
        "sid": "7d946861e6b2d74b2db38a442a19fd38",
        "token": "8712938e22c34a179b3cea43ff783b68",
        "appid": "0e6c046983c74d59948cd381e814503d",
        "templateid": "422930",  # 模板id
        "param": vcode,  # 验证码，自己生成
        "mobile": phone,  # 接收短信的手机号
    }

    response = requests.post(url, json=param)
    return response.text


def gen_vcode():
    '''
    生成随机6位的验证码
    '''
    vcode = ""
    for _ in range(6):
        vcode += str(random.randint(0, 9))
    return vcode


# 封装： 函数 => 类 => 模块 => 包
if __name__ == '__main__':
    vcode = gen_vcode()
    ret = send_sms('18566218480', vcode)
    print(ret)


