from sqlalchemy import create_engine
import os


# file_path = os.path.abspath(__file__)


class Database:
    def __init__(self):
        self.db = create_engine("sqlite:///db/test.db")

    def connect(self):
        return self.db.connect()

    def disconnect(self):
        self.db.dispose()


global db

db = Database()




