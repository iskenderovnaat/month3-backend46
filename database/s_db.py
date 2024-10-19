import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS survey_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone_number TEXT,  
                    visit_date TEXT,    
                    food_rating TEXT,
                    cleanliness_rating TEXT,
                    review_extra_comments TEXT,
                    tg_id INTEGER
                )
            """)
            connection.commit()

    def execute(self, query: str, params: tuple = ()):
        with sqlite3.connect(self.path) as connection:
            connection.execute(query, params)
            connection.commit()