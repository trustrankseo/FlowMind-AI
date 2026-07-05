class ApiInfo:

    def info(self):

        return {
            "name": "FlowMind AI",
            "version": "1.0.0",
            "docs": "/docs",
            "redoc": "/redoc",
            "health": "/health"
        }


api_info = ApiInfo()