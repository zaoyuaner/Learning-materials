"""
异步
"""
import tornado.web
import tornado.ioloop
import tornado.httpclient


class IndexHandler(tornado.web.RequestHandler):
    # asynchronous异步话，io连接不能自动关闭，需要等到回调成功后才关闭
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        wd = self.get_argument('wd')
        # 获取客户端
        client = tornado.httpclient.AsyncHTTPClient()
        # 回调callback
        client.fetch('https://cn.bing.com/search?q=' + wd,
                     callback=self.on_response)
        print('异步操作')
        self.write('异步操作')

    def on_response(self, response):
        print(response)
        print('异步回调')
        self.write('异步回调')
        # 关闭io
        self.finish()


def make_app():
    return tornado.web.Application(handlers=[
        ('/index/', IndexHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()




