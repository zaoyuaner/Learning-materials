
from flask import Blueprint, render_template

# from back.models import Article

web_blue = Blueprint('web',__name__)


@web_blue.route('/index/', methods=['GET'])
def index():
    # articles = Article.query.limit(14).all()
    return render_template('web/index.html')


@web_blue.route('/about/', methods=['GET'])
def about():
    return render_template('web/about.html')


@web_blue.route('/gbook/', methods=['GET'])
def gbook():
    return render_template('web/后期制作/gbook.html')

@web_blue.route('/info/', methods=['GET'])
def info():
    return render_template('web/info.html')

@web_blue.route('/infopic/', methods=['GET'])
def infopic():
    return render_template('web/后期制作/infopic.html')

@web_blue.route('/list/', methods=['GET'])
def list():
    return render_template('web/list.html')

@web_blue.route('/share/', methods=['GET'])
def share():
    return render_template('web/后期制作/share.html')





@web_blue.route('/base/', methods=['GET'])
def base():
    return render_template('web/base_main.html')






