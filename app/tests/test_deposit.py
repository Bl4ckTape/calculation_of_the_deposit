
import json


def test_positive_deposit(test_client, test_valid_formdata):
    response = test_client.post('/api/deposit', json=test_valid_formdata)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert test_valid_formdata["periods"] == len(data.keys())


def test_negative_calc_deposit(test_client, test_not_valid_formdata):
    response = test_client.post("/api/deposit", json=test_not_valid_formdata)
    assert response.status_code == 400
    data = json.loads(response.data.decode())
    assert data['amount'] == ['This field is required.']
    assert data['rate'] == ['This field is required.']


def test_validate_deposit_date(test_client, test_not_valid_date):
    response = test_client.post('/api/deposit', json=test_not_valid_date)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["date"] == ["Incorrect data format, should be dd.mm.YYYY"]


def test_validate_periods(test_client, test_not_valid_periods):
    response = test_client.post('/api/deposit', json=test_not_valid_periods)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["periods"] == ["Number must be between 1 and 60."]


def test_validate_deposit_amount(test_client,
                                 test_not_valid_amount):
    response = test_client.post('/api/deposit', json=test_not_valid_amount)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["amount"] == ["Number must be between 10000 and 3000000."]


def test_validate_deposit_rate(test_client, test_not_valid_rate):
    response = test_client.post('/api/deposit', json=test_not_valid_rate)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["rate"] == ["Number must be between 1 and 8."]
