from pydantic.main import BaseModel

class BaseOutputModel():
    def __init__(self):
        self.status = 0
        self.message = ""
        self.result = {}