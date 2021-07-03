from fastapi.param_functions import Query
from Server.Model.BaseModel.PageModel import PageModel
from Server.Model.BaseOutputModel import BaseOutputModel
from Server.Model.BaseModel.ProductModel import ProductModel
from Server.Repository.ProductRepository import ProductRepository

###############################################################################

RepProduct = ProductRepository()

###############################################################################

async def product_insert(body:ProductModel) -> BaseOutputModel:
    retVal = BaseOutputModel()
    try:
        if RepProduct.Insert(body.getInsertJson()) == False:
            retVal.message = "failed inserting product"
            retVal.status = 0
            return retVal
        retVal.message = "product inserted"
        retVal.result = body.getInsertJson()
        retVal.status = 1
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

    
async def product_get_all(body:PageModel) -> BaseOutputModel:
    retVal = BaseOutputModel()
    page, size = body.pageNumber, body.pageSize
        
    itemlen = RepProduct.GetCount()
    total_page = int(itemlen/size) if itemlen%size==0 else int(itemlen/size)+1

    paged_item = []
    for i in RepProduct.GetPages(pageNum=page, pageSize=size):
        paged_item.append({
            "_id":str(i["_id"]),
            "productName":i["productName"],
            "thumbnailUrl":i["thumbnailUrl"],
            "price":i["price"]
        })

    retVal.result = {
        "totalPage":total_page,
        "pageNumber":page,
        "pageSize":size,
        "items":paged_item
    }
    return retVal