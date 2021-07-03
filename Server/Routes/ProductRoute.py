## Package Import ##
from Server.Model.BaseModel.PageModel import PageModel
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
## AppCode Import ##
from Server.Controller.ProductController import *
from Server.Model.BaseModel.ProductModel import *
from Server.Utility.JWT import JWTBearer

###############################################################################

ProductRoute = APIRouter()

###############################################################################

@ProductRoute.post("/product/insert")
async def insert_product(body: ProductModel) -> BaseOutputModel:
    return await product_insert(body);

@ProductRoute.post("/product/getall")
async def get_all_product(body: PageModel) -> BaseOutputModel:
    return await product_get_all(body)
