from pydantic import (
    BaseModel,
    Field
)


class AssetCreate(BaseModel):

    asset_name: str = Field(..., min_length=3)

    asset_tag: str = Field(..., min_length=3)

    asset_type: str

    serial_number: str = Field(..., min_length=3)

    status: str
