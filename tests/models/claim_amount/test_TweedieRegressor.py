import pytest
import exceptions

from models.claim_amount.tweedie_regressor import TweedieClaimModel


def test_model_init():
    model = TweedieClaimModel()

    assert model.name == "Tweedie Claim Model"


def test_batch_prediction():
    model = TweedieClaimModel()
    y_pred = model.batch_predict(car_make="BZ", car_year=2000, n_simulations=1000)

    assert len(y_pred.tolist()) == 1000


def test_batch_prediction_with_invalid_car_year():
    model = TweedieClaimModel()

    with pytest.raises(exceptions.CarYearException):
        y_pred = model.batch_predict(car_make="BZ", car_year=2025, n_simulations=100)

