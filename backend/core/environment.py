import platform
import sys


class Environment:

    def info(self):

        return {
            "python_version": sys.version,
            "python_major": sys.version_info.major,
            "python_minor": sys.version_info.minor,
            "platform": platform.system(),
            "platform_release": platform.release(),
            "architecture": platform.machine()
        }


environment = Environment()