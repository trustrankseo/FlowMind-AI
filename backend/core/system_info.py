import os


class SystemInfo:

    def info(self):

        return {
            "cwd": os.getcwd(),
            "environment_variables": len(os.environ)
        }


system_info = SystemInfo()