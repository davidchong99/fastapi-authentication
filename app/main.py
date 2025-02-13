import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse

from app.auth_jwt.authentication import authenticate_request as jwt_auth
from app.auth_api_key.authentication import authenticate_request as api_key_auth
from app.organization_router import organization
from app.metric_router import metric

from app.env import SETTINGS


# Create app
app = FastAPI(title="Authentication API", version="1.0.0")

app.include_router(
    organization.router, prefix="/organization", dependencies=[Depends(jwt_auth)]
)
app.include_router(
    metric.router, prefix="/metrics", dependencies=[Depends(api_key_auth)]
)


@app.get("/", response_class=PlainTextResponse)
def get_root():
    return "Root ..."


if __name__ == "__main__":
    # Start server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=SETTINGS.server_port,
        log_level=SETTINGS.server_log_level,
    )
