import pytest
import exceptions

from models.claim_amount.tweedie_regressor import TweedieClaimModel


def test_model_init():
    model = TweedieClaimModel()
    print("\n", model.name)
    assert model.name == "Tweedie Claim Model"


def test_model_prediction():
    model = TweedieClaimModel()
    y_pred = model.predict(car_make="BZ", car_year=2000)

    assert y_pred.tolist() == [1.051]


def test_model_prediction_with_invalid_car_year():
    model = TweedieClaimModel()

    with pytest.raises(exceptions.CarYearException):
        y_pred = model.predict(car_make="BZ", car_year=2025)

