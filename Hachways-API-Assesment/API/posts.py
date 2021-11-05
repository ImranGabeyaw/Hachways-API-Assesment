import requests

class Posts:
	def _simple_request(tag):
		API = 'https://api.hatchways.io/assessment/blog/posts'
		API += '?tag=' + tag
		r = requests.get(url=API)
		return r.json()

	def _unique_merge(result1, result2):
		if not result1:
			return result2
		if not result2:
			return result1

		for item in result2:
			if item not in result1:
				result1.append(item)
		return result1

	def _sort_result(result, sortBy, direction):
		if direction == 'desc':
			result.sort(key=lambda x: x[sortBy], reverse=True)
		else:
			result.sort(key=lambda x: x[sortBy])
		return result

	@classmethod
	def make_request(cls, tags, sortBy='id', direction='asc'):
		combined_result = []
		split_tags = tags.split(',')
		for tag in split_tags:
			combined_result=cls._unique_merge(combined_result, cls._simple_request(tag)['posts'])

		combined_result=cls._sort_result(combined_result, sortBy, direction)

		response = {}
		response["posts"] = combined_result
		return response
