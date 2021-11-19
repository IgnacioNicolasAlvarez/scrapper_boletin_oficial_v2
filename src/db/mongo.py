from pymongo import MongoClient


def conectar_a_mongo(username, password, host, port):
    cliente = MongoClient(
        f"mongodb+srv://{username}:{password}@{host}.mongodb.net",
        port,
    )
    return cliente


def conectar_a_db(cliente, db_name):
    db = cliente[db_name]
    return db
