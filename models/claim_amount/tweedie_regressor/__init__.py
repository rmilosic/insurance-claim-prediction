from exceptions import CarYearException
from models import FeaturesData

import os
from datetime import datetime
from joblib import load
import pandas as pd
import numpy as np
from db import db

dirname = os.path.dirname(__file__)


class TweedieClaimModel:
    def __init__(self, name="Tweedie Claim Model"):

        self.name = name

        artifacts_path = os.path.join(dirname, './artifacts')
        self.col_transformer = load(os.path.join(artifacts_path, "column_transformer_2020-05-31 19:09.joblib"))
        self.model = load(os.path.join(artifacts_path, "Tweedie_Regressor_2020-05-31 19:09.joblib"))

        df = FeaturesData.load()
        # build empty dictionary from features
        self.features_names = df.columns
        self.features_data = df.to_records()

    def batch_predict(self, car_make, car_year, n_simulations):
        """
        Predicts the expected claim amount from inputs and random sampling
        from other independent variables

        Parameters
        ----------
        car_make: str
            encoded car make ("AK")
        car_year: int
            e.g. 2000
        n_simulations: int
            number of random samples

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

        # create new dataframe with sampling of original features
        df = pd.DataFrame(
            columns=self.features_names,
            data=self.features_data
        )
        # sample from df based on n_simulations
        df = df.sample(
            n=n_simulations,
            axis=0,
            replace=False
        )
        # overwrite input parameters
        df["Car_Age"] = car_age
        df["Blind_Make"] = car_make

        print(df)
        X_tf = self.col_transformer.transform(df)

        y_pred = self.model.predict(X_tf)

        return np.round(a=y_pred, decimals=3)


