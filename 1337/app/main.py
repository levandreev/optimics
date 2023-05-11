from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
from models.models import ArticleCreate
from models.models import Article, Session

app = FastAPI()

@app.get("/authors", response_model=List[str])
def get_authors():
    session = Session()
    authors = session.query(Article.author).distinct().all()
    session.close()
    author_list = [author[0] for author in authors]
    return JSONResponse(content=author_list)

@app.get("/urls", response_model=List[str])
def get_urls(url: str = None):
    session = Session()
    if url:
        urls = session.query(Article.url).distinct().filter(Article.url == url).all()
    else:
        urls = session.query(Article.url).distinct().all()   
    session.close()
    url_list = [url[0] for url in urls]
    return JSONResponse(content=url_list)

@app.get("/articles")
def get_articles():
    session = Session()
    articles = session.query(Article).all()
    session.close()
    article_list = []
    for article in articles:
        article_dict = {
            'id': article.id,
            'title': article.title,
            'published_date': article.published_date.isoformat(),
            'author': article.author,
            'author_link': article.author_link,
            'url': article.url
        }
        article_list.append(article_dict)
    return JSONResponse(content=article_list)

@app.get("/articles/{article_id}")
def get_article(article_id: int):
    session = Session()
    article = session.query(Article).filter_by(id=article_id).first()
    session.close()
    if article is None:
        return JSONResponse(content={'error': 'Article not found'}, status_code=404)
    article_dict = {
        'id': article.id,
        'title': article.title,
        'published_date': article.published_date.isoformat(),
        'author': article.author,
        'author_link': article.author_link,
        'url': article.url
    }
    return JSONResponse(content=article_dict)

@app.post("/articles")
def create_article(article: ArticleCreate):
    session = Session()
    new_article = Article(
        title=article.title,
        published_date=article.published_date,
        author=article.author,
        author_link=article.author_link,
        url=article.url,
    )
    session.add(new_article)
    session.commit()
    session.refresh(new_article)
    created_article = {
        'id': new_article.id,
        'title': new_article.title,
        'published_date': str(new_article.published_date),
        'author': new_article.author,
        'author_link': new_article.author_link,
        'url': new_article.url
    }
    session.close()
    return JSONResponse(content=created_article, status_code=201)

@app.put("/articles/{article_id}")
def update_article(article_id: int, article: ArticleCreate):
    session = Session()
    existing_article = session.query(Article).filter_by(id=article_id).first()
    if existing_article is None:
        return JSONResponse(content={'error': 'Article not found'}, status_code=404)
    # Update the article fields only if they are provided
    if article.title:
        existing_article.title = article.title
    if article.published_date:
        existing_article.published_date = article.published_date
    if article.author_link:
        existing_article.author_link = article.author_link
    if article.url:
        existing_article.url = article.url
    session.commit()
    updated_article = {
        'id': existing_article.id,
        'title': existing_article.title,
        'published_date': str(existing_article.published_date),
        'author': existing_article.author,
        'author_link': existing_article.author_link,
        'url': existing_article.url
    }
    session.close()
    return JSONResponse(content=updated_article)

@app.delete("/articles/{article_id}")
def delete_article(article_id: int):
    session = Session()
    existing_article = session.query(Article).filter_by(id=article_id).first()
    if existing_article is None:
        return JSONResponse(content={'error': 'Article not found'}, status_code=404)
    session.delete(existing_article)
    session.commit()
    session.close()
    return JSONResponse(content={'message': 'Article deleted successfully'})
