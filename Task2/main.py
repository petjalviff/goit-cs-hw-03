from db import get_database
from models import add_cat, find_all_cats, update_cat_age, add_feature_to_cat, find_cat_by_name, delete_cat_by_name, delete_all_cats

def main():
    """Головна функція, яка демонструє роботу з базою даних котів."""
    db = get_database()
    if db is not None: 
        input("Press Enter to add a cat...")
        add_cat(db, "Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])

        input("Press Enter to display all cats...")
        find_all_cats(db)

        input("Press Enter to update a cat's age...")
        update_cat_age(db, "Barsik", 4)

        input("Press Enter to add a feature to a cat...")
        add_feature_to_cat(db, "Barsik", "любить спати")

        input("Press Enter to find a specific cat by name...")
        find_cat_by_name(db, "Barsik")

        input("Press Enter to delete a specific cat by name...")
        delete_cat_by_name(db, "Barsik")

        input("Press Enter to delete all cats...")
        delete_all_cats(db)

if __name__ == "__main__":
    main()
