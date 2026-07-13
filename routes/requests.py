from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.service_request import ServiceRequest
from models.asset import Asset

from schemas.service_request import ServiceRequestCreate

from services.request_service import (
    valid_request_status,
    valid_priority,
    get_resolution_date
)

router = APIRouter(
    prefix="/requests",
    tags=["Service Requests"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_request(
    request: ServiceRequestCreate,
    db: Session = Depends(get_db)
):

    asset = db.query(Asset).filter(
        Asset.id == request.asset_id
    ).first()

    if not asset:

        raise HTTPException(
            status_code=404,
            detail="Asset not found."
        )

    if not valid_priority(request.priority):

        raise HTTPException(
            status_code=400,
            detail="Invalid priority."
        )

    if not valid_request_status(request.status):

        raise HTTPException(
            status_code=400,
            detail="Invalid request status."
        )

    new_request = ServiceRequest(
        employee_id=request.employee_id,
        asset_id=request.asset_id,
        issue_title=request.issue_title,
        description=request.description,
        priority=request.priority,
        status=request.status,
        resolution_date=get_resolution_date(request.status)
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    return new_request


@router.get("/")
def get_requests(
    employee_id: int = None,
    asset_id: int = None,
    priority: str = None,
    status: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(ServiceRequest)

    if employee_id:
        query = query.filter(
            ServiceRequest.employee_id == employee_id
        )

    if asset_id:
        query = query.filter(
            ServiceRequest.asset_id == asset_id
        )

    if priority:
        query = query.filter(
            ServiceRequest.priority == priority
        )

    if status:
        query = query.filter(
            ServiceRequest.status == status
        )

    total = query.count()

    requests = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": requests
    }


@router.get("/{request_id}")
def get_request(
    request_id: int,
    db: Session = Depends(get_db)
):

    request = db.query(ServiceRequest).filter(
        ServiceRequest.id == request_id
    ).first()

    if not request:

        raise HTTPException(
            status_code=404,
            detail="Service request not found."
        )

    return request


@router.put("/{request_id}")
def update_request(
    request_id: int,
    request: ServiceRequestCreate,
    db: Session = Depends(get_db)
):

    db_request = db.query(ServiceRequest).filter(
        ServiceRequest.id == request_id
    ).first()

    if not db_request:

        raise HTTPException(
            status_code=404,
            detail="Service request not found."
        )

    if db_request.status == "Closed":

        raise HTTPException(
            status_code=400,
            detail="Closed requests cannot be updated."
        )

    db_request.issue_title = request.issue_title
    db_request.description = request.description
    db_request.priority = request.priority
    db_request.status = request.status
    db_request.resolution_date = get_resolution_date(
        request.status
    )

    db.commit()

    return {
        "message": "Service request updated successfully."
    }


@router.post("/{request_id}/assign/{support_id}")
def assign_request(
    request_id: int,
    support_id: int,
    db: Session = Depends(get_db)
):

    request = db.query(ServiceRequest).filter(
        ServiceRequest.id == request_id
    ).first()

    if not request:

        raise HTTPException(
            status_code=404,
            detail="Service request not found."
        )

    request.support_id = support_id
    request.status = "Assigned"

    db.commit()

    return {
        "message": "Request assigned successfully."
    }


@router.get("/support/{support_id}/requests")
def support_requests(
    support_id: int,
    db: Session = Depends(get_db)
):

    return db.query(ServiceRequest).filter(
        ServiceRequest.support_id == support_id
    ).all()
