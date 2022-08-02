from datetime import date
from datetime import datetime

def string_to_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

def date_to_string(data: date) -> str:
    return data.strftime('%d/%m/%Y')

def float_to_string(valor: float) -> str:
    return f'R$ {valor:,.2f}'