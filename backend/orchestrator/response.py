class ResponseBuilder:

    def build(
        self,
        response: str,
        data: dict
    ):

        return {
            "success": True,
            "response": response,
            "data": data
        }


response_builder = ResponseBuilder()