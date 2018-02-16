#! /usr/bin/python

# import modules
import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

# flask object
app = Flask(__name__)
api = Api(app)

# get posts
class posts(Resource):
	def get(self):
		# connect to db
		conn = sqlite3.connect('blog.db')

		# set cursor
		c = conn.cursor()

		# query string
		posts = conn.execute("select * from posts").fetchall()

		# close db connection
		conn.close

		# display blog posts
		return posts

# create post
class post(Resource):
	def post(self):
		# connect to db
		conn = sqlite3.connect('blog.db')
		c = conn.cursor()

		# parser for args
		parser = reqparse.RequestParser()
		parser.add_argument('title', type=str)
		parser.add_argument('body', type=str)
		args = parser.parse_args()
		
		# args
		title = str(args['title']).strip()
		body = str(args['body']).strip()
		postid = c.lastrowid

		# queries
		query = "insert into posts values(?,?,?)"
		query = conn.execute(query, (postid,title,body))

		# commit and close db connection
		conn.commit()
		conn.close()

		# confirmation message 
		return 'Blog post has been successfully submitted.'

# api resources
api.add_resource(post, '/post')
api.add_resource(posts, '/posts')

# run app locally on port 8080
if __name__ == '__main__':
	app.run(host="127.0.0.1",debug=True,port=int('8080'))
