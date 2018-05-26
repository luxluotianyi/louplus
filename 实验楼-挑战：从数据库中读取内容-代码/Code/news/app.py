import os
import json
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/web'
db = SQLAlchemy(app)

class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	category = db.relationship('Category', backref=db.backref('articls', lazy="dynamic"))
	content = db.Column(db.Text)
	def __init__(self, title, created_time, category, content):
		self.title = title
		if created_time is None:
			created_time = datetime.utcnow()
		self.created_time = created_time
		self.category = category
		self.content = content

	def __repr__(self):
		return '%s' % self.title


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '%s' % self.name


@app.route('/')
def index():
	title_list = Article.query.all()
	return render_template('index.html',title_list=title_list)

@app.route('/files/<int:file_id>')
def file(file_id):
	file_item = Article.query.filter_by(id=file_id).first()
	if not file_item:
		abort(404)
	return render_template('file.html',file_item=file_item)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404




if __name__ == '__main__':
	app.run()
