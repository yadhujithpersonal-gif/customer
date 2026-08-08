from pydantic import BaseModel


class DisputeCreate(BaseModel):

    customer_id: str

    order_id: str

    message: str