import json
from random import randrange

from sqlalchemy.orm import sessionmaker

from bot.services.database.db import engine, Quote


def create_session():
    session = sessionmaker(bind=engine)
    return session()


def add_quote(quote):
    s = create_session()
    temp_quote = Quote(quote=quote)
    s.add(temp_quote)
    s.commit()


def is_in_db(quote):
    s = create_session()
    return True if s.query(Quote).filter(Quote.quote == quote).first() else False


def all_quotes():
    s = create_session()
    quotes = {}
    for quote in s.query(Quote).all():
        quotes[quote.quote] = str(quote.quote)
    return quotes


def random_quote():
    s = create_session()
    num_of_quotes = s.query(Quote).count()
    return s.query(Quote).filter(Quote.quote_id == randrange(1, num_of_quotes)).first().quote


def load_example_data():
    file = open('bot/resources/example_data.json', encoding='utf-8')
    data = json.load(file)
    for quote in data['quotes']:
        add_quote(quote)
