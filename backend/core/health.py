from backend.core.container import container
from backend.core.version import VERSION, BUILD
from backend.core.startup_check import startup_check
from backend.core.environment import environment
from backend.core.dependency_check import dependency_check
from backend.core.system_info import system_info
from backend.core.app_status import app_status


def system_health():

    return {
        "status": "healthy",
        "version": VERSION,
        "build": BUILD,
        "application": app_status.info(),
        "services": list(container.all().keys()),
        "startup": startup_check.run(),
        "environment": environment.info(),
        "dependencies": dependency_check.run(),
        "system": system_info.info(),
    }