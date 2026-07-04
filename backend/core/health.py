from backend.core.container import container


def system_health():

    return {
        "services": list(container.all().keys()),
        "status": "healthy"
    }