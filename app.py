# encoding:utf-8
from flask import Flask, url_for, redirect, session, make_response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/')
def hello_world():
    # print(url_for('article',number='123456'))
    # login_url=url_for('my_list')
    # return redirect(login_url)
    class Person():
        name = 'liangboxn'
        age = 22

    p = Person()

    context = {
        'name': 'boxin',
        'age': 21,
        'gender': '男',
        'person': p,
        'websites': {
            'baidu': '<a href=' + "http://www.baidu.com/" + '>百度</a>',
            'google': '<a href="http://www.google.com/">谷歌</a>'
        }
    }
    return render_template('index.html', **context)

# 这是登陆链接
@app.route('/list/')
def my_list():
    user = {
        'name': 'daweiwang',
        'age': 20
    }
    return render_template('login.html', user=user)


@app.route('/article/<number>')
def article(number):
    # #增加：
    # article1 = Article(title='how to xxoo',content='您想 how to play %s ' % number)
    # db.session.add(article1)
    # #事务的提交
    # db.session.commit()
    result = Article.query.filter(Article.title=="how to xxoo").all()
    print(result[0])
    return '您请求的参数是: %s' % result[0]

# 这是发布问题链接
@app.route('/question/<is_login>')
def question(is_login):
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', name)
    if is_login == '1'and name == 'boxin':
        return '这是%s发布问题页面' % name.upper()
    elif is_login == '1'or name == 'boxin':
        return redirect(url_for('my_list'))
    # session[]=True
    return '这页面是提问题的: %s' % is_login

# 这是设置cookie的链接
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('my_list')))
    response.set_cookie('name', name)
    return response

#
@app.route('/home')
def home():
    user = {
        'username': '一拳超人',
        'age': 27
    }
    websites = ['baidu.com', 'google.com']

    return render_template('home.html', user=user, websites=websites)


@app.route('/books')
def book():
    classicbook = [
        {
            'bookname': '西游记',
            'author': '吴承恩',
            'price': 150
        },
        {
            'bookname': '红楼梦',
            'author': '曹雪芹',
            'price': 200
        },
        {
            'bookname': '三国演义',
            'author': '罗贯中',
            'price': 160

        },
        {
            'bookname': '水浒传',
            'author': '施耐庵',
            'price': 130
        }
    ]

    return render_template('home.html', classicbook=classicbook)


@app.route('/picture')
def picture():
    context = [
        {
            'name': 'zhiniaoketang',
            'content': '妖神记'
        }, {
            'name': 'mituyoufang',
            'content': '食戟之灵'
        }
    ]
    return render_template(
        'filter.html',
        avater='https://edu-image.nosdn.127.net/37b647007b764cf2ab6d779b865e869c.jpg?imageView&quality=100&crop=0_1_879_494&thumbnail=450y250',
        context=context)


if __name__ == '__main__':
    app.run()
