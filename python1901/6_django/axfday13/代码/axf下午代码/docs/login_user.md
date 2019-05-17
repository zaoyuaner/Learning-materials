### 登录接口

#### 请求地址: /api/user/auth/login/

#### 请求方式: POST

#### 请求参数:

    u_username  登录账号  string  必填
    u_password  登录密码  string  必填
    
#### 响应

##### 1. 响应成功

    {
        code: 200,
        msg: '请求成功',
        data: {
            token: gaywifgqu365082q
        }
    }
    
##### 2. 失败响应

    {
        'code': 1004, 
        'msg': '登录账号不存在，请更换账号'
    }

    {
        'code': 1005, 
        'msg': '登录密码错误'
    }

    {
        'code': 1006,
         'msg': '登录参数有误'
    }
    
#### 响应参数
    
    code 状态码  int
    msg  响应信息  string
    token 登录标识符  string



