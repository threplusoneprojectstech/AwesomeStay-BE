## Package Import ##
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
## AppCode Import ##
from Server.Controller.ProductController import *
from Server.Model.BaseModel.ProductModel import *
from Server.Model.BaseModel.PageModel import PageModel
from Server.Utility.JWT import JWTBearer

###############################################################################

ProductRoute = APIRouter()

###############################################################################

@ProductRoute.post("/product/insert")
async def insert_product(body: ProductModel) -> BaseOutputModel:
    return await product_insert(body);

@ProductRoute.post("/product/getpages")
async def get_pages_product(body: PageModel) -> BaseOutputModel:
    return await product_get_pages(body)

@ProductRoute.post("/product/getdetails")
async def get_product_detail(body: ProductDetailRequestModel):
    return await product_get_details(body)
