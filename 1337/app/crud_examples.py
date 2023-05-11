import requests
from models.models import Article
from fastapi.encoders import jsonable_encoder

# CREATE
new_article = Article(
    title="New article 2",
    published_date="2023-04-24T11:42:44.942000+02:00",
    author="John Doe",
    author_link="https://johndoe.com",
    url="https://johndoe.com/new-article"
)
article_id = 73

new_article_dict = jsonable_encoder(new_article)

response = requests.post(
    'http://localhost:8000/articles', json=new_article_dict
)

if response.status_code == 201:
    print('Article created successfully')
else:
    print('1')

# READ
response = requests.get(
    'http://localhost:8000/articles'
)

if response.status_code == 200:
    print('Article list returned successfully')
else:
    print('2')

response = requests.get(
    'http://localhost:8000/articles/{}'.format(article_id)
)

if response.status_code == 200:
    print('Article {} returned successfully'.format(article_id))
else:
    print('Failed to create article')


# UPDATE
updated_article = Article(
    title="Some updated article",
)

response = requests.put(
    'http://localhost:8000/articles/{}'.format(article_id), json=jsonable_encoder(updated_article)
)
if response.status_code == 200:
    print('Article {} updated successfully'.format(article_id))
else:
    print('Failed to update article')

# DELETE

article_id = 87
response = requests.delete(
    'http://localhost:8000/articles/{}'.format(article_id)
)
if response.status_code == 200:
    print('Article {} deleted successfully'.format(article_id))
else:
    print('Failed to delete article')
