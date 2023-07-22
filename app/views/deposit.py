import datetime
import json
from flask import jsonify
from app.forms import DepositForm
from flask import Blueprint, Response
from dateutil.relativedelta import relativedelta

api_bp = Blueprint('api', __name__)


@api_bp.route('/api/deposit', methods=['post'])
def deposit():
    form = DepositForm()
    if form.validate_on_submit():
        date = form.date.data
        periods = form.periods.data
        amount = form.amount.data
        rate = form.rate.data

        percent = 1 + rate / 12 / 100
        date_start = datetime.datetime.strptime(date, "%d.%m.%Y")

        deposits = {}
        for i in range(periods):
            date = date_start + relativedelta(months=+i)
            date_str = date.strftime("%d.%m.%Y")
            amount = round(amount * percent, 2)
            deposits[date_str] = amount
        return deposits
    return Response(json.dumps(form.errors), status=400)
