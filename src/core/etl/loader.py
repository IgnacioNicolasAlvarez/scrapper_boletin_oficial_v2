
from src.db.postgre import insert


def save_data(data: list):
    for i in data:
        insert(i)