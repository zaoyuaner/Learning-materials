import os

import tornado.web
import tornado.ioloop

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.render('login.html')

    def post(self, *args, **kwargs):
        # 模拟登陆
        username = self.get_argument('username')
        password = self.get_argument('password')
        if not (username and password):
            self.render('login.html', error='账号和密码必填')
        if not(username == 'coco' and password == '123456'):
            self.render('login.html', error='账户或密码有误')
        self.set_cookie('username', username)
        self.render('chat.html')

def make_app():
    # 获取day03的绝对路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # BASE_DIR = os.path.dirname(__file__)
    return tornado.web.Application(handlers=[
        ('/login/', LoginHandler),
    ],
    template_path=os.path.join(BASE_DIR, 'templates'),
    static_path=os.path.join(BASE_DIR, 'static')
    )

if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

