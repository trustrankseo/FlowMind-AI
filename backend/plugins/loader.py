from pathlib import Path
import importlib


class PluginLoader:

    def __init__(self):
        self.plugins = {}

    def discover(self):

        plugins_dir = Path(__file__).parent

        for item in plugins_dir.iterdir():

            if (
                item.is_dir()
                and (item / "__init__.py").exists()
            ):

                module = importlib.import_module(
                    f"backend.plugins.{item.name}"
                )

                if hasattr(module, "plugin"):

                    self.plugins[item.name] = module.plugin

    def all(self):

        return self.plugins


plugin_loader = PluginLoader()