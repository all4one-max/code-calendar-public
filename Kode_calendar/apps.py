from django.apps import AppConfig


class KodeCalendarConfig(AppConfig):
    name = "Kode_calendar"

    def ready(self):
        from .api_scheduler import contest_updater

        contest_updater.start()