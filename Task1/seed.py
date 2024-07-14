import psycopg2
from faker import Faker
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random

# Параметри підключення до бази даних
host = "localhost"
database = "postgres"
user = "postgres"
password = "mysecretpassword"

# Об'єкт Faker
fake = Faker()

def populate_database():
    # Підключення до бази даних
    with psycopg2.connect(host=host, database=database, user=user, password=password) as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with conn.cursor() as cur:
            # Додавання користувачів
            insert_user_query = "INSERT INTO users (fullname, email) VALUES (%s, %s)"
            for _ in range(100):
                fullname = fake.name()
                if random.choice([True, False]):
                    user_number = random.randint(1, 99)
                    email = f"{fullname.lower().replace(' ', '.')}{user_number}@example.com"
                else:
                    email = f"{fullname.lower().replace(' ', '.')}@example.com"
                cur.execute(insert_user_query, (fullname, email))

            # Додавання статусів
            status_names = ['new', 'in progress', 'completed']
            insert_status_query = "INSERT INTO status (name) VALUES (%s)"
            cur.executemany(insert_status_query, [(name,) for name in status_names])

            # Додавання завдань
            insert_task_query = "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"
            for _ in range(300):
                title = fake.sentence(nb_words=6).rstrip('.')
                description = fake.sentence(nb_words=15)
                status_id = fake.random_int(min=1, max=3)
                user_id = fake.random_int(min=1, max=100)
                cur.execute(insert_task_query, (title, description, status_id, user_id))

if __name__ == "__main__":
    populate_database()