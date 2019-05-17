import random
import requests
from chaojiying import Chaojiying_Client

# 1， 保存登录成功后的cookie
# 2， 使用保存的cookie进行登录， 登录后获取个人信息
# 	 url = "http://www.renren.com/548819077/profile"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

# 登录
def login(code):
    # 人人网登录接口：
    url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201905945581"
    # 参数：
    data = {
        "email": "gaohj5@163.com",
        "icode": code,
        "origURL": "http://www.renren.com/home",
        "domain": "renren.com",
        "key_id": "1",
        "captcha_type": "web_login",
        "password": "46e515b20f9d67e9480bb43466a5ced7e3060624125f3b3286f88583de3bc3f0",
        "rkey": "通过fidder",
        "f": "",
    }

    response = session.post(url, data=data, headers=headers)
    result = response.content.decode()
    print(result)


# 获取验证码,并破解
def get_code():
    # 获取验证码接口
    url = "http://icode.renren.com/getcode.do?t=web_login&rnd=%s" % str(random.random())
    res = session.get(url, headers=headers)
    # 下载图片
    with open('code.jpg', 'wb') as fp:
        fp.write(res.content)
        fp.flush()

    # 破解验证码
    chaojiying = Chaojiying_Client(soft_id='898304')
    im = open('code.jpg', 'rb').read()
    result = chaojiying.PostPic(im, 2004)['pic_str']
    print(result)
    return result


# # 人人网个人中心
def get_profile():
    url = "http://www.renren.com/541197383/profile"
    response2 = session.get(url, headers=headers)
    print(response2.text)

if __name__ == '__main__':

    session = requests.session()

    # 获取验证码
    code = get_code()

    # 登录
    login(code)

    # 登录后再访问个人中心
    get_profile()







