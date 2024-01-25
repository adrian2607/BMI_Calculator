from datetime import datetime
import sqlite3
from typing import Optional

def get_time_and_date() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class DataStorage:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        try:
            self.connection = sqlite3.connect('bmi_results.db')
            self.create_table()
        except sqlite3.Error as e:
            print(e)

    def create_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bmi_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    weight REAL,
                    height REAL,
                    bmi REAL,
                    classification TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def save_to_database(self, weight: float, height: float, bmi: float, classification: str, date: Optional[str] = None) -> None:
        try:
            if date is None:
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO bmi_results (timestamp, weight, height, bmi, classification)
                VALUES (?, ?, ?, ?, ?)
            ''', (date, weight, height, bmi, classification))

            self.connection.commit()
            print("BMI result saved to the database.")
        except sqlite3.Error as e:
            print(e)

    def save_to_file(self, data: str) -> None:
        with open("bmi_results.txt", "a") as file:
            file.write(data + "\n")
