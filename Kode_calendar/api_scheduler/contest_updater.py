from apscheduler.schedulers.background import BackgroundScheduler
from Kode_calendar.views import api_calling

from datetime import datetime, timedelta


def start():
    scheduler = BackgroundScheduler()
    instance = api_calling()
    scheduler.add_job(
        instance.site_call,
        "interval",
        seconds=60,
        id="api_001",
        replace_existing=True,
    )
    scheduler.start()
