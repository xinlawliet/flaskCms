from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(5), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref =db.backref('articles'))

#多对多进行关系映射
art_tag = db.Table('art_tag',
                   db.Column('art_id',db.Integer,db.ForeignKey('art.id'),primary_key=True),
                   db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)
                   )

class Art(db.Model):
    __tablename__ = 'art'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    #中间的是关系表，关系表最后为一个变量的形式。
    tags = db.relationship('Tag',secondary=art_tag,backref = db.backref('articles'))

class Tag(db.Model):
    __tablename__ = 'tag'
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)


