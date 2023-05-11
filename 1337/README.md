# 1337

This API is built with FastAPI and SQLAlchemy and uses a PostgreSQL database to store articles from [novinky.cz](https://novinky.cz)

## Prerequisites

Python 3.11.0 or higher
PostgreSQL database
## Usage

1. Install dependencies:

```shell
$ pip install -r requirements.txt
```

2. Start the server:

```shell
$ uvicorn main:app --reload
```

3. Start the scraper:

```shell
python scraper.py
```

In a root directory of the project create a `.env` file that will have path to your PostgreSQL connection string 
`DATABASE_URL = postgresql://[user[:password]@][netloc][:port][/dbname]`

You can refer to `crud_examples.py` module to see how to use the API.
## Model

### Article

Represents an article in the database. An article has the following attributes:

- `id` (`int`): the unique identifier of the article.
- `title` (`str`): the title of the article.
- `published_date` (`DateTime`): the publication date of the article.
- `author` (`str`): the author of the article.
- `author_link` (`str`): the URL of the author's website.
- `url` (`str`): the URL of the article.

## Endpoints

### `GET /articles`

Returns a list of all articles in the database.

#### Response

- `200 OK`: returns a JSON list of article objects.

##### Example

```json
[
  {
    "id": 1,
    "title": "KVÍZ: Jak se vyznáte v lidském mozku a jeho funkcích? ",
    "published_date": "2023-04-22T12:30:00",
    "author": "Dana Sokolová",
    "author_link": "https://www.novinky.cz/autor/dana-klejnova-18",
    "url": "https://www.novinky.cz/clanek/zena-zdravi-kviz-jak-se-vyznate-v-lidskem-mozku-a-jeho-funkcich-40429403"
  },
  {
    "id": 2,
    "title": "Na dálnici D35 spadl z vleku bagr",
    "published_date": "2023-04-22T12:15:18.876000",
    "author": null,
    "author_link": null,
    "url": "https://www.novinky.cz/clanek/krimi-na-dalnici-spadl-bagr-40429431"
  }
]
```

### `GET /articles/{article_id}`

Returns a specific article.

#### Response

- `200 OK`: returns a JSON object representing the article.
- `404 Not Found`

### `GET /authors`

Returns a list of distinct authors in the database.

#### Response

- `200 OK`: returns a JSON list of strings representing the authors

##### Example

```json
[
  "Andrea Zunová",
  "Zdeněk Smíšek",
  "Ondřej Kořínek",
  "Jindřich Ginter",
  "Pavel Cechl",
  "Marek Bádal",
  "Martin Dohnal ",
  "Filip Šára",
  "Ivan Vilček"
]
```

### `GET /urls`

Returns a list of distinct article URLs in the database.

#### Parameters

- `url` (optional) : a string representing the URL to filter by.

#### Response

- `200 OK`: returns a JSON list of strings representing the URLs

##### Example

```json
[
  "https://www.novinky.cz/clanek/zahranicni-zabery-z-dramaticke-honicky-s-paseraky-drog-na-mori-u-mallorky-policie-zabavila-vic-nez-tunu-hasise-40429632",
  "https://www.novinky.cz/clanek/auto-elektricky-liftback-lotusu-pri-testech-na-nurburgringu-odhalil-hodne-navzdory-maskovani-40429605"
]
```

### `POST /articles`

This endpoint creates a new article.
#### Reqest Body
- `ArticleCreate` object: Contains the fields for creating a new article.

#### Response

- `201 Created`: Returns a JSON object with the fields of the created article.

### `PUT /articles/{article_id}`
This endpoint updates the article with the given ID.
- article_id (required): ID of the article
#### Reqest Body
- `ArticleCreate` object: Contains the fields for creating a new article.
#### Response

- `200 OK`: returns a JSON object representing the article.
- `404 Not Found`

### `DELETE /articles{article_id}`
This endpoint deletes the article with the given ID.
- article_id (required): ID of the article

