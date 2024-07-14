from pymongo.errors import PyMongoError
import logging

def add_cat(db, name, age, features):
    """Додає нового кота до бази даних."""
    try:
        cat_collection = db["cats"]
        cat_document = {"name": name, "age": age, "features": features}
        result = cat_collection.insert_one(cat_document)
        if result.acknowledged:
            logging.info("Cat %s added with ID: %s", name, result.inserted_id)
        else:
            logging.warning("Failed to add cat due to unacknowledged result")
    except PyMongoError as e:
        logging.error("Failed to add cat: %s", e)
        return None
    return result.inserted_id

def find_all_cats(db):
    """Знаходить усіх котів у базі даних та повертає їх список."""
    try:
        cat_collection = db["cats"]
        cats = list(cat_collection.find({}))
        logging.info("All cats retrieved successfully")
        for cat in cats:
            logging.info(cat)
    except PyMongoError as e:
        logging.error("Failed to retrieve cats: %s", e)
        return []
    return cats

def find_cat_by_name(db, name):
    """Знаходить кота за заданим іменем та повертає його документ."""
    try:
        cat_collection = db["cats"]
        cat = cat_collection.find_one({"name": name})
        if cat:
            logging.info("Cat found: %s", cat)
        else:
            logging.info("No cat found with that name.")
    except PyMongoError as e:
        logging.error("Failed to find cat by name: %s", e)
        return None
    return cat

def update_cat_age(db, name, age):
    """Оновлює вік кота з заданим іменем."""
    try:
        cat_collection = db["cats"]
        result = cat_collection.update_one({"name": name}, {"$set": {"age": age}})
        if result.modified_count > 0:
            logging.info("Updated cat %s's age to %s", name, age)
        else:
            logging.info("No updates made. Cat may not exist.")
    except PyMongoError as e:
        logging.error("Failed to update cat's age: %s", e)
        return 0
    return result.modified_count

def add_feature_to_cat(db, name, feature):
    """Додає нову рису до кота з заданим іменем."""
    try:
        cat_collection = db["cats"]
        result = cat_collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count > 0:
            logging.info("Added feature '%s' to cat %s", feature, name)
        else:
            logging.info("No updates made. Cat may not exist.")
    except PyMongoError as e:
        logging.error("Failed to add feature to cat: %s", e)
        return 0
    return result.modified_count

def delete_cat_by_name(db, name):
    """Видаляє кота з заданим іменем з бази даних."""
    try:
        cat_collection = db["cats"]
        result = cat_collection.delete_one({"name": name})
        if result.deleted_count > 0:
            logging.info("Deleted cat %s successfully", name)
        else:
            logging.info("No cat deleted. Cat may not exist.")
    except PyMongoError as e:
        logging.error("Failed to delete cat: %s", e)
        return 0
    return result.deleted_count

def delete_all_cats(db):
    """Видаляє усіх котів з бази даних."""
    try:
        cat_collection = db["cats"]
        result = cat_collection.delete_many({})
        if result.deleted_count > 0:
            logging.info("All cats deleted. Count: %s", result.deleted_count)
        else:
            logging.info("No cats deleted.")
    except PyMongoError as e:
        logging.error("Failed to delete all cats: %s", e)
        return 0
    return result.deleted_count
