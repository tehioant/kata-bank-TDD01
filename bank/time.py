import datetime


class TimeService:

    def get_time_now() -> datetime:
        return datetime.datetime.now()
