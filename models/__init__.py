import pandas as pd

from db import db


class FeaturesData:

    @staticmethod
    def load():
        try:
            # create connection to sqlite db file
            conn = db.connect()

            # load feature data from sqlite
            df = pd.read_sql_table(
                table_name="features",  # table name
                con=conn
            )
            return df
        except Exception as e:
            raise e
        finally:
            conn.close()
