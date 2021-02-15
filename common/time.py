from datetime import datetime, timedelta


def now():
    return datetime.utcnow() + timedelta(hours=8)
