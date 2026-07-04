from backend.core.container import container
from backend.core.version import VERSION, BUILD


def system_health():

    return {
        "status": "healthy",
        "version": VERSION,
        "build": BUILD,
        "services": list(container.all().keys())
    }