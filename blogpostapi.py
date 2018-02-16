#! /usr/bin/python

# import modules
import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine

# sqlite engine
e = create_engine('sqlite:///blog.db')

# flask object
app = Flask(__name__)
api = Api(app)

# get posts
class posts(Resource):
	def get(self):
		# connect to db
		conn = e.connect()
		# query string
		query = conn.execute("select * from posts")
		results = []
		for row in query.cursor.fetchall():
			results += [{'post_id': str(row[0]), 'title': str(row[1]), 'body': str(row[2])}]
		return results

# create post
class post(Resource):
	def post(self):
		# connect to db
		conn = e.connect()
		curs = conn.cursor()

		# parser for args
		parser = reqparse.RequestParser()
		parser.add_argument('title', type=str)
		parser.add_argument('body', type=str)
		args = parser.parse_args()
		
		# args
		title = str(args['title']).strip()
		body = str(args['body']).strip()
		postid = curs.lastrowid

		# queries
		query = "insert into posts values(?,?,?)"
		query = conn.execute(query, (postid,title,body))

		# results
		return 'Blog post has been successfully submitted.'

# api resources
api.add_resource(post, '/post')
api.add_resource(posts, '/posts')

# run app locally on port 8080
if __name__ == '__main__':
	app.run(host="127.0.0.1",debug=True,port=int('8080'))
