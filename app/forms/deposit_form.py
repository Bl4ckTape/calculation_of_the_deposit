from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange, ValidationError

import datetime


class DepositForm(FlaskForm):
    date = StringField(
        'Дата заявки',
        validators=[DataRequired()]
    )
    periods = IntegerField(
        'Количество месяцев по вкладу',
        validators=[DataRequired(), NumberRange(min=1, max=60)]
    )
    amount = IntegerField(
        'Сумма вклада',
        validators=[DataRequired(), NumberRange(min=10000, max=3000000)]
    )
    rate = FloatField(
        'Процент по вкладу',
        validators=[DataRequired(), NumberRange(min=1, max=8)]
    )

    class Meta:
        csrf = False

    def validate_date(self, field):
        try:
            datetime.datetime.strptime(field.data, "%d.%m.%Y")
            return field
        except ValueError as e:
            raise ValidationError(
                "Incorrect data format, should be dd.mm.YYYY") from e
