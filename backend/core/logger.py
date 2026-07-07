import logging
from collections import deque


class MemoryLogHandler(logging.Handler):
    """
    Keeps the last N log records in memory so the dashboard's Logs panel
    has something real to display, without needing a separate log
    aggregation service.
    """

    def __init__(self, capacity: int = 300):
        super().__init__()
        self.capacity = capacity
        self.records = deque(maxlen=capacity)

    def emit(self, record):

        self.records.append({
            "time": self.format(record).split(" | ")[0],
            "level": record.levelname,
            "message": record.getMessage()
        })

    def recent(self, limit: int = 100):
        return list(self.records)[-limit:]


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("FlowMind")

memory_log_handler = MemoryLogHandler()
memory_log_handler.setFormatter(
    logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
)
logger.addHandler(memory_log_handler)
