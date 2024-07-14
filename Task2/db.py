from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_database():
    """Повертає об'єкт бази даних MongoDB для подальшої роботи."""
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        logging.info("Database connected successfully")
    except ConnectionFailure as e:
        logging.error("Failed to connect to database: %s", e)
        return None
    return client["cat_database"]
