from datetime import datetime


def format_datetime(d: datetime) -> str:
    return d.strftime("%Y-%m-%d %H:%M:%S")


def format_time(d: datetime) -> str:
    return d.strftime("%H:%M")
