#!/usr/bin/env python3

from flask import Flask, render_template, request, abort
import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
	files = os.listdir('/home/shiyanlou/files')
	jsondata = []
	for file in files:
		with open('/home/shiyanlou/files/'+file) as f:
			jsondata.append(json.loads(f.read()))
	return	render_template('index.html', data=jsondata)

@app.route('/files/<filename>')
def file(filename):
	
	files = os.listdir('/home/shiyanlou/files')
	if filename+'.json' not in files:
		abort(404)
	for file in files:
		if filename+'.json' == file:
			with open('/home/shiyanlou/files/'+file) as f:
				filedata = json.loads(f.read())
	return render_template('file.html',data=filedata)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run()
