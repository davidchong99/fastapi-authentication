from fastapi import APIRouter, status, Depends, HTTPException
from app.auth_api_key.authentication import authenticate_request as api_key_auth
from app.metric_router import service
from app.auth_api_key.authentication import authenticate_request as api_key_auth

from app.metric_router.dto import MetricData

router = APIRouter()


@router.get(
    "/get_metric/{id}",
    response_model=MetricData,
)
def get_metric(
    id: int,
    authenticated: bool = Depends(api_key_auth),
):
    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    return service.get_metric(id)
