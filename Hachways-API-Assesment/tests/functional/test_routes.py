from API import routes, app
from flask import Flask



def test_ping():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/api/ping')
        assert response.status_code == 200
        assert {"success": "true"} == response.get_json()

def test_posts_tags():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/posts?tags=history,tech' page is requested (GET)
    THEN check that the response is valid by having one of the named tags
    """
    

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/api/posts?tags=history,tech')
        assert response.status_code == 200
        for item in response.get_json()['posts']:
            assert 'history' or 'tech' in item['tags']

def test_posts_tags_sort():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/posts?tags=history,tech&sortBy=id' page is requested (GET)
    THEN check that the response is valid by having one of the named tags as well as sorted by id
    """
    

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/api/posts?tags=history,tech&sortBy=id')
        assert response.status_code == 200
        posts=response.get_json()['posts']
        for i in range(len(posts)-1):
            assert posts[i]['id'] < posts[i+1]['id']

def test_posts_tags_sort_direction():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/posts?tags=history,tech&sortBy=id&direction=desc' page is requested (GET)
    THEN check that the response is valid by having one of the named tags as well as sorted by id in descending order
    """
    

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/api/posts?tags=history,tech&sortBy=id&direction=desc')
        assert response.status_code == 200
        posts=response.get_json()['posts']
        for i in range(len(posts)-1):
            assert posts[i]['id'] > posts[i+1]['id']

def test_posts_sortBy_valid():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/posts?tags=history,tech&sortBy=id' page is requested (GET)
    THEN check that the response is valid by having one of the named tags as well as sorted by id
    """
    

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/api/posts?tags=history,tech&sortBy=iddf')

        assert response.status_code == 400
        posts=response.get_json()
        print(posts)
        assert posts == {"error": "sortBy parameter is invalid"}