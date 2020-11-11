from database import Database
from os import getenv


def save(category: str, url: str):
    db = Database(getenv('DB_NAME'))
    return db.insert('urls', None, category, url)


def fetch_categories():
    db = Database(getenv('DB_NAME'))
    return db.fetch_distinct('urls', 'category')


def fetch_urls(category: str):
    db = Database(getenv('DB_NAME'))
    return db.fetch_all('urls', category=category)