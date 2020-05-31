from argparse import ArgumentParser
import sqlite3

import pandas as pd

conn = sqlite3.connect('db/test.db')   # You can create a new database by changing the name within the quotes
c = conn.cursor()


def main(file_path):
    # load csv file
    df = pd.read_csv(file_path, encoding="utf-8")
    print(df.head())

    # write file to connection, drop table before writing
    df.to_sql(
        name="original_data",    # table name
        con=conn,                # connection
        if_exists="replace",
        index=False
    )
    print(f"file at path {file_path} successfully writen to sqlite db"
    )




if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-f", dest="file_path", action="store", required=True, type=str, help="only csv files are allowed")
    args = parser.parse_args()

    main(args.file_path)

