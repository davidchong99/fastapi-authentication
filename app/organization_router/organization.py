from fastapi import APIRouter, status, Depends, HTTPException

from app.auth_jwt.authentication import authenticate_request as jwt_auth
from app.auth_jwt.dto import Identity
from app.organization_router import service
from app.organization_router.dto import Organization

router = APIRouter()


@router.get(
    "/get_organization",
    response_model=Organization,
)
def get_employee(
    user: Identity = Depends(jwt_auth),
):
    if "read" not in user.permissions:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not permitted",
        )

    return service.get_organization(user)
