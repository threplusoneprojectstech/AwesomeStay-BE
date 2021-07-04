from bson.objectid import ObjectId
from Server.Model.ProductRequestModel import ProductDetailRequestModel
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

    
async def product_get_pages(body:PageModel) -> BaseOutputModel:
    retVal = BaseOutputModel()
    try:
        page, size = body.pageNumber, body.pageSize
            
        itemlen = RepProduct.GetCount()
        total_page = int(itemlen/size) if itemlen%size==0 else int(itemlen/size)+1

        paged_item = []
        for i in RepProduct.GetPages(pageNum=page, pageSize=size):
            i["_id"] = str(i["_id"])
            paged_item.append(i)

        retVal.result = {
            "totalPage":total_page,
            "pageNumber":page,
            "pageSize":size,
            "items":paged_item
        }
        retVal.status = 1
        retVal.message = "success"
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal

async def product_get_details(body:ProductDetailRequestModel):
    retVal = BaseOutputModel()
    try:
        query = { "$and": [
            { "_id" : ObjectId(body.id) }
        ] }
        data = RepProduct.GetOne(query)
        if data == None:
            retVal.message = "product not found"
            retVal.status = 0
            return retVal
        data["_id"] = str(data["_id"])
        retVal.message = "success"
        retVal.status = 1
        retVal.result = data
        return retVal
    except:
        retVal.message = "API error"
        retVal.status = 0
        return retVal