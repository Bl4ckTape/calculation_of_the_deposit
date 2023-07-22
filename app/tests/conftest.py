import pytest
from app.main import app as flask_app


@pytest.fixture(scope='module')
def test_client():
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture
def test_valid_formdata():
    return {"date": "22.07.2023", "periods": 5, "amount": 10000, "rate": 6}


@pytest.fixture
def test_not_valid_formdata():
    return {"date": "31.01.2021", "periods": 7}


@pytest.fixture
def test_not_valid_date():
    return {"date": "22/07/2023", "periods": 5, "amount": 10000, "rate": 6}


@pytest.fixture
def test_not_valid_periods():
    return {"date": "22.07.2023", "periods": 61, "amount": 10000, "rate": 6}


@pytest.fixture
def test_not_valid_amount():
    return {"date": "22.07.2023", "periods": 5, "amount": 1000, "rate": 6}


@pytest.fixture
def test_not_valid_rate():
    return {"date": "22.07.2023", "periods": 5, "amount": 10000, "rate": 9}
