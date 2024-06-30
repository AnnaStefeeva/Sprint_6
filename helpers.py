from datetime import datetime, timedelta


def generate_date(days_from_now):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_from_now)
    return future_date.strftime('%d.%m.%Y')
