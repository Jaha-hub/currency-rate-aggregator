from apscheduler.schedulers.background import BackgroundScheduler
from app.api.test import update_rates

scheduler = BackgroundScheduler()

scheduler.add_job(
    update_rates,
    "interval",
    hours=24
)