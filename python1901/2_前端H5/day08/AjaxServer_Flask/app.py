from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/movies/')
def movies():
    page = request.args.get('page')
    if not page:
        return "请填写page参数"

    page = int(page) - 1
    if page < 0 or page > 4 :
        return "页码page范围是：1~5"

    with open('json/movies.json') as fp:
        content = fp.read()
        movie_list = json.loads(content)

        return jsonify(movie_list[page])

    return 'Hello World!'

@app.route('/movies2/')
def movies2():
    page = request.args.get('page')
    if not page:
        return "请填写page参数"

    page = int(page) - 1
    if page < 0 or page > 4 :
        return "页码page范围是：1~5"

    with open('json/movies2.json') as fp:
        content = fp.read()
        movie_list = json.loads(content)

        return jsonify(movie_list[page])

    return 'Hello World!'


@app.route('/register/', methods=['get', 'post'])
def register():
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    if not (name and pwd):
        return "用户名或密码未填写"

    with open('json/users.json') as fp:
        content = fp.read()
        user_list = json.loads(content)

        for user in user_list:
            if name == user['name']:
                return jsonify({'msg': 'register error!用户名已经存在，请重新填写'})

        user_list.append({'name': name, 'pwd': pwd})

    with open('json/users.json', 'w') as fp:
        fp.write(json.dumps(user_list))
        return jsonify({'msg': 'register success!'})


@app.route('/login/',  methods=['get', 'post'])
def login():
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    if not (name and pwd):
        return "用户名或密码未填写"

    with open('json/users.json') as fp:
        content = fp.read()
        user_list = json.loads(content)

        for user in user_list:
            if user['name'] == name and user['pwd'] == pwd:
                return jsonify({'msg': 'login success'})
        return jsonify({'msg': 'login failed! 用户名或密码错误'})


if __name__ == '__main__':
    app.run(host='0')
