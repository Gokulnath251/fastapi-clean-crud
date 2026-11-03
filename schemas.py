from pydantic import BaseModel, Field, ConfigDict

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)
    cost_price: float = Field(..., gt=0)
    in_stock: bool = True

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    cost_price: float | None = None
    in_stock: bool | None = None

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

    model_config = ConfigDict(from_attributes=True)
