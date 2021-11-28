
from src.db.postgre import insert


def save_en_postgres(object):
    insert(object)