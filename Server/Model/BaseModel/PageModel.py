from pydantic import BaseModel

class PageModel(BaseModel):
    pageNumber:int
    pageSize:int