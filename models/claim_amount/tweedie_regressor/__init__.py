import os
from datetime import datetime
from joblib import load
import pandas as pd
import numpy as np
from db import db

dirname = os.path.dirname(__file__)
from exceptions import CarYearException


class TweedieClaimModel:
    def __init__(self, name="Tweedie Claim Model"):

        self.name = name

        artifacts_path = os.path.join(dirname, './artifacts')
        self.col_transformer = load(os.path.join(artifacts_path, "column_transformer_2020-05-31 19:09.joblib"))
        self.model = load(os.path.join(artifacts_path, "Tweedie_Regressor_2020-05-31 19:09.joblib"))

        try:
            # create connection to sqlite db file
            conn = db.connect()

            # load feature data from sqlite
            df = pd.read_sql_table(
                table_name="features",  # table name
                con=conn
            )
        except Exception as e:
            raise e
        finally:
            conn.close()

        # build empty dictionary from features
        self.features = {col: np.nan for col in df.columns}

    def predict(self, car_make, car_year):
        """
        Predicts the expected claim amount from inputs

        Parameters
        ----------
        car_make: str
            encoded car make ("AK")
        car_year: int
            e.g. 2000

        Returns
        ---------
        ev: float
            best model prediction of expected value
        """

        # get this year
        this_year = datetime.now().year

        if car_year > this_year:
            raise CarYearException("Car Year should be equal or less to this year")

        # get age from this year and registration year
        car_age = this_year - car_year

        features = self.features.copy()

        features["Car_Age"] = car_age
        features["Blind_Make"] = car_make

        X = pd.DataFrame(
            index=[0],
            columns=features.keys(),
            data=features
        )

        print(X)
        X_tf = self.col_transformer.transform(X)

        y_pred = self.model.predict(X_tf)

        return np.round(a=y_pred, decimals=3)


