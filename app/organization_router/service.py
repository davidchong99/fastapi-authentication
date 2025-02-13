from app.auth_jwt.dto import Identity
from app.organization_router.dto import Organization


def get_organization(user: Identity) -> Organization:
    return Organization(org=user.organization)
