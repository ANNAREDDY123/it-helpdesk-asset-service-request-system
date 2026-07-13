from sqlalchemy import (
    Column,
    Integer,
    String
)

from database import Base


class Asset(Base):

    __tablename__ = "assets"

    id = Column(
        Integer,
        primary_key=True
    )

    asset_name = Column(String)

    asset_tag = Column(
        String,
        unique=True
    )

    asset_type = Column(String)

    serial_number = Column(String)

    status = Column(String)
