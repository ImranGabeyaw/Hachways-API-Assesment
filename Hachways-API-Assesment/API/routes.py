from flask import Flask, request
from .posts import Posts
from .validation import validate_query
from . import app

@app.route("/api/ping")
def ping():
	return {"success": "true"}

@app.route("/api/posts")
def posts():
	args = request.args

	error_check = validate_query(args)
	if error_check is not None:
		return error_check[0], error_check[1]

	sortBy = 'id'
	direction = 'asc'
	if 'sortBy' in args:
		sortBy = args['sortBy']
	if 'direction' in args:
		direction = args['direction']
		
	return Posts.make_request(args['tags'], sortBy, direction)
