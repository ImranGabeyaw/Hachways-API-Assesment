import requests

class Posts:
	def _simple_request(tag):
		API = 'https://api.hatchways.io/assessment/blog/posts'
		API += '?tag=' + tag
		r = requests.get(url=API)
		return r.json()

	def _unique_merge(cache, result1, result2):
		if not result1:
			for item in result2:
				if item['id'] not in cache:
					cache[item['id']] = item['id']
					result1.append(item)
			return cache, result1
		if not result2:
			return cache, result1

		for item in result2:
			if item['id'] not in cache:
				cache[item['id']] = item['id']
				result1.append(item)
		return cache, result1

	def _sort_result(result, sortBy, direction):
		if direction == 'desc':
			result.sort(key=lambda x: x[sortBy], reverse=True)
		else:
			result.sort(key=lambda x: x[sortBy])
		return result

	@classmethod
	def make_request(cls, tags, sortBy='id', direction='asc'):
		combined_result = []
		cache = dict()
		split_tags = tags.split(',')
		for tag in split_tags:
			cache, combined_result=cls._unique_merge(cache, combined_result, cls._simple_request(tag)['posts'])

		combined_result=cls._sort_result(combined_result, sortBy, direction)

		response = {}
		response["posts"] = combined_result
		return response
