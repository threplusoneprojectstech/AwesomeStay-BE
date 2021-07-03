from pydantic import BaseModel

class ProductModel(BaseModel):
    productName:str
    thumbnailUrl:str
    price:float
    description:str
    morePictureUrl:list
    location:str
    rating:float
    userRateCount:int
    userReview:list
    facility:list
    stock:int

    def getInsertJson(this):
        return {
            "productName":this.productName,
            "thumbnailUrl":this.thumbnailUrl,
            "price":this.price,
            "description":this.description,
            "morePictureUrl":this.morePictureUrl,
            "location":this.location,
            "rating":this.rating,
            "userReview":this.userReview,
            "facility":this.facility,
            "stock":this.stock
        }