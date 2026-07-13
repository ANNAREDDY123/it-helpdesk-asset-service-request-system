from pydantic import (
    BaseModel,
    Field
)


class ServiceRequestCreate(BaseModel):

    employee_id: int

    asset_id: int

    issue_title: str = Field(..., min_length=3)

    description: str = Field(..., min_length=5)

    priority: str

    status: str
