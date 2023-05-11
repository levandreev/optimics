import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from models.models import Article
from fastapi.encoders import jsonable_encoder


def get_news_urls(sitemap_url: str) -> List[str]:
    response = requests.get(sitemap_url)
    if response.status_code != 200:
        print(
            f"Failed to fetch the sitemap with status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "xml")

    # Initialize an empty list to store the dictionaries
    news_list = []

    # Iterate through all <url> elements in the XML
    for url_element in soup.find_all("url"):
        # Find the <loc>, <news:publication_date>, and <news:title> elements
        loc = url_element.find("loc")
        publication_date = url_element.find("news:publication_date")
        title = url_element.find("news:title")

        # Create a dictionary for the current <url> element
        news_dict = {
            "url": loc.text if loc else "",
            "publication_date": publication_date.text if publication_date else "",
            "title": title.text if title else "",
        }

        # Append the dictionary to the news_list
        news_list.append(news_dict)

    return news_list


def process_sitemap_urls(sitemap_urls: List[str]):
    for article in sitemap_urls:
        response = requests.get(article['url'])
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            try:
                section = soup.find('section')
                divs = section.find_all('div') if section else None
                title = divs[0].find('h1').text
                try:
                    author = divs[1].find('div').find_all(
                        'div')[1].find_all('div')[1].find_all('a')[0].text
                    author_link = divs[1].find('div').find_all(
                        'div')[1].find_all('div')[1].find_all('a')[0]['href']
                except:
                    print('author doesnt exist for ' + article['url'])
                    author = None
                    author_link = None
            except Exception as err:
                print('something went wrong')
                continue

            new_article = Article(
                title=title,
                published_date=article['publication_date'],
                author=author,
                author_link=author_link,
                url=article['url']
            )

            # Check if an article with the same URL already exists in the database
            article_not_exists = (requests.get(
                'http://localhost:8000/urls?url=' + article['url'])).text == '[]'
            print(article_not_exists)
            if article_not_exists:
                response = requests.post(
                    'http://localhost:8000/articles', json=jsonable_encoder(new_article))
                if response.status_code == 201:
                    print('Article saved successfully')
                else:
                    print('Failed to save article')


if __name__ == '__main__':
    # see https://www.novinky.cz/robots.txt
    sitemap_url = "https://www.novinky.cz/sitemaps/sitemap_news.xml"
    articles = get_news_urls(sitemap_url)
    process_sitemap_urls(articles)
