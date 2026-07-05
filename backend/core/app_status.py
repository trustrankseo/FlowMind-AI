from datetime import datetime


class AppStatus:

    def __init__(self):
        self.started_at = datetime.utcnow()

    def info(self):

        uptime = datetime.utcnow() - self.started_at

        return {
            "started_at": self.started_at.isoformat(),
            "uptime_seconds": int(uptime.total_seconds())
        }


app_status = AppStatus()