"""
同步
"""
import tornado.web
import tornado.ioloop
import tornado.httpclient


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 获取客户端
        wd = self.get_argument('wd')
        client = tornado.httpclient.HTTPClient()
        response = client.fetch('https://cn.bing.com/search?q=' + wd)
        print(response)
        self.write('同步操作')

def make_app():
    return tornado.web.Application(handlers=[
        ('/index/', IndexHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
