class ServiceContainer:

    def __init__(self):
        self._services = {}

    def register(self, name: str, service):

        self._services[name] = service

    def get(self, name: str):

        return self._services.get(name)

    def has(self, name: str):

        return name in self._services

    def all(self):

        return self._services


container = ServiceContainer()