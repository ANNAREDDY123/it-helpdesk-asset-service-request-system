from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from database import Base


class ServiceRequest(Base):

    __tablename__ = "service_requests"

    id = Column(
        Integer,
        primary_key=True
    )

    employee_id = Column(Integer)

    asset_id = Column(
        Integer,
        ForeignKey("assets.id")
    )

    support_id = Column(Integer)

    issue_title = Column(String)

    description = Column(String)

    priority = Column(String)

    status = Column(String)

    resolution_date = Column(Date)
