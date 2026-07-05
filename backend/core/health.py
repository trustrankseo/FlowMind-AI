from backend.core.container import container
from backend.core.version import VERSION, BUILD
from backend.core.startup_check import startup_check


def system_health():

    return {
        "status": "healthy",
        "version": VERSION,
        "build": BUILD,
        "services": list(container.all().keys()),
        "startup": startup_check.run()
    }