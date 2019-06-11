# encoding:utf-8
from flask import Flask, url_for, redirect, session, make_response, request, render_template
import config
from model import db, Art, User, Article,Tag
app = Flask(__name__)
app.config.from_object(config)
# 数据库初始化
db.init_app(app)
#db.create_all()



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
    # user2 = User(username='计算机',sex='男')
    # db.session.add(user2)
    # db.session.commit()
    #
    # article = Article(title='网易云', content='付费充值',author_id=3)
    # db.session.add(article)
    # db.session.commit()

    # article2 =Article.query.filter(Article.title=='科学与技术').first()
    #     # author_id = article2.author_id
    #     # user2 = User.query.filter(User.id == author_id).first()
    #     # print(user2.username)

    # article3 = Article.query.filter(Article.title == '网易云').first()
    # print(article3.author.username)

    otheruser = User.query.filter(User.id == 3).first()
    result = otheruser.articles
    print(len(result))
    for i in range(len(result)):
        print("作者%s有书籍%d--%s" % (otheruser.username, i+1, result[i].title))

    return render_template('login.html', user=user,result=result,otheruser =otheruser)


@app.route('/article/<number>')
def article(number):

    #增加：
    # article1 = Article(title='display your life',content='您想 how to play %s ' % number)
    # article2 =Article()
    # article2.title ='应届大学生'
    # article2.content ='00后准大学生'
    # db.session.add(article1)
    # db.session.add(article2)
    # #事务的提交
    # db.session.commit()

    #all查询所有记录，first查询第一条记录，此时可以用对象.属性的方式查询，all的时候就不可以。
    #get方法不用filter过滤条件
    result = Article.query.filter(Article.title=="how to xxoo").first()
    print(result)
    #print(result[0])
    #print(result.content)

    #修改属性
    #result.title='今天是端午节，也是高考的日子'
    #print(result.title)
    # db.session.commit()

    #删除，先查询出来，然后删除提交
    result2 = Article.query.get(9)
    print(result2)
    db.session.delete(result2)
    db.session.commit()
    return '您请求的参数是: %s' % number

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
     #新建两篇文章
    art1 = Art(title='大海')
    art2 = Art(title='小人')
     #新建两个标签
    tag1 = Tag(name='酸')
    tag2 = Tag(name='甜')

    #添加多对多关系,文章1添加两个标签
    art1.tags.append(tag1)
    art1.tags.append(tag2)
    # 添加多对多关系,文章2添加两个标签
    art2.tags.append(tag1)
    art2.tags.append(tag2)


    #添加部分
    db.session.add(art1)
    db.session.add(art2)
    db.session.add(tag1)
    db.session.add(tag2)

    db.session.commit()
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
