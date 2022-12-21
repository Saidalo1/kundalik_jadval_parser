from datetime import datetime


def date(time: str):
    return datetime.now().strftime(time)
