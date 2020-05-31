import exceptions
import pytest


def f(exception):
    raise exception


def test_CarYearException():
    with pytest.raises(exceptions.CarYearException):
        f(exceptions.CarYearException)