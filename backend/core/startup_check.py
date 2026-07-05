from importlib import import_module


class StartupCheck:

    MODULES = [
        "backend.core.container",
        "backend.core.bootstrap",
        "backend.engine.engine",
        "backend.providers.provider_manager",
        "backend.services.chat_service",
        "backend.database.session",
    ]

    def run(self):

        results = []

        for module in self.MODULES:

            try:

                import_module(module)

                results.append({
                    "module": module,
                    "status": "OK"
                })

            except Exception as e:

                results.append({
                    "module": module,
                    "status": "ERROR",
                    "error": str(e)
                })

        return results


startup_check = StartupCheck()