import os

import tornado.web
import tornado.ioloop
import tornado.websocket


# from tornado.options import define, options,parse_command_line

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        # 模拟登录
        username = self.get_argument('username')
        password = self.get_argument('password')
        if not (username and password):
            error = '账号密码必填'
            self.render('login.html', error=error)
        if not(username in ['花花', 'coco', 'xml'] and password == '123123'):
            error = '账号或密码有问题'
            self.render('login.html', error=error)
            # 可以登录，状态保持
        self.set_secure_cookie('username', username)
        self.render('chat.html')


class ChatHandler(tornado.websocket.WebSocketHandler):
    users = []
    def open(self, *args, **kwargs):
        # 存储长连接
        self.users.append(self)
        # username = self.get_cookie('username')
        username = self.get_secure_cookie('username').decode('utf8')
        for user in self.users:
            user.write_message('[{}]欢迎登录系统'.format(username))



    def on_message(self, message):
        username = self.get_secure_cookie('username').decode('utf8')
        # 接收前端给后发送的内容
        for user in self.users:
            user.write_message('[{}]:{}'.format(username,message))

    def on_close(self):
        # 关闭连接时候调用
        self.users.remove(self)
        username = self.get_cookie('username')
        for user in self.users:
            user.write_message('[{}]已退出系统'.format(username))






def make_app():
    # BASE_DIR = os.path.dirname(__file__)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return tornado.web.Application(handlers=[
        ('/login/', LoginHandler),
        ('/chat/', ChatHandler)
    ],
        template_path=os.path.join(BASE_DIR, 'templates'),
        static_path=os.path.join(BASE_DIR, 'static'),
        cookie_secret='sdfs@#d#g$^5fdDfg234'

    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
