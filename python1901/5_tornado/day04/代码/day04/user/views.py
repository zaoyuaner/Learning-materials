
import tornado.web

from user.models import create_db, User
from utils.conn import session
from utils.faceid import register_face_user


class RegisterHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        self.render('register.html')

    def post(self, *args, **kwargs):
        # 获取数据
        face = self.get_argument('face')
        username = self.get_argument('username')
        # 人脸注册
        img = face.split(',')[-1]
        if not register_face_user(img, username):
            self.render('register.html', error='注册失败')
        user = User()
        user.username = username
        session.add(user)
        session.commit()
        self.write('注册成功')



class InitDBHandler(tornado.web.RequestHandler):
     def get(self):
         create_db()
         self.write('初始化数据库成功')
