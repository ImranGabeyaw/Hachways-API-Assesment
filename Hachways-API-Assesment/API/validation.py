
def validate_query(query):
	valid_sort = ['id', 'reads', 'likes', 'popularity']
	valid_direction = ['asc', 'desc']

	if 'tags' not in query:
		return {"error": "tags parameter is required"}, 400
	if 'sortBy' in query and query['sortBy'] not in valid_sort:
		return {"error": "sortBy parameter is invalid"}, 400
	if 'direction' in query and query['direction'] not in valid_direction:
		return {"error": "direction parameter is invalid"}, 400

	return None
