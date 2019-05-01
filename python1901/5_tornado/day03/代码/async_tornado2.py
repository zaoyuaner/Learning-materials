"""
协程
"""
import tornado.web
import tornado.ioloop
import tornado.httpclient

class IndexHandler(tornado.web.RequestHandler):

    @tornado.web.gen.coroutine
    def get(self, *args, **kwargs):
        wd = self.get_argument('wd')
        client = tornado.httpclient.AsyncHTTPClient()
        print('协程')
        response = yield client.fetch('https://cn.bing.com/search?q=' + wd)
        print(response)
        self.write('协程')

def make_app():
    return tornado.web.Application(handlers=[
        ('/index/', IndexHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

