import os

import tornado.web
import tornado.ioloop
import tornado.websocket

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.render('login.html')

    def post(self, *args, **kwargs):
        # 模拟登陆
        username = self.get_argument('username')
        password = self.get_argument('password')
        if not (username and password):
            self.render('login.html', error='账号和密码必填')
        if not(username in ['小明', 'coco', 'admin', 'vincent'] and password == '123456'):
            self.render('login.html', error='账户或密码有误')
        # self.set_cookie('username', username)
        self.set_secure_cookie('username', username)
        self.render('chat.html')


class ChatHandler(tornado.websocket.WebSocketHandler):

    users = []
    def open(self, *args, **kwargs):
        # 将建立的长连接存起来
        self.users.append(self)
        # username = self.get_cookie('username')
        username = self.get_secure_cookie('username').decode('utf8')
        for user in self.users:
            user.write_message('【%s】欢迎登录系统' % username)

    def on_message(self, message):
        # 接收前端给后端发送的内容
        username = self.get_cookie('username')
        for user in self.users:
            user.write_message('【%s】: %s' % (username, message))

    def on_close(self):
        # 关闭连接时调用
        self.users.remove(self)
        username = self.get_cookie('username')
        for user in self.users:
            user.write_message('【%s】已退出系统' % username)


def make_app():
    # 获取day03的绝对路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # BASE_DIR = os.path.dirname(__file__)
    return tornado.web.Application(handlers=[
        ('/login/', LoginHandler),
        ('/chat/', ChatHandler),
    ],
    template_path=os.path.join(BASE_DIR, 'templates'),
    static_path=os.path.join(BASE_DIR, 'static'),
    cookie_secret='oyrowyhfjskjhsjdhfjs'
    )

if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

