from fastapi import APIRouter

from app.api.endpoints import (
    charity_project_router, donation_router, google_api_router, user_router
)

CHARITY_PROJECT_PREFIX = '/charity_project'
CHARITY_PROJECT_TAGS = ['charity_projects']
DONATION_PREFIX = '/donation'
DONATION_TAGS = ['donations']
GOOGLE_PREFIX = '/google'
GOOGLE_TAGS = ['Google']

main_router = APIRouter()
main_router.include_router(
    charity_project_router,
    prefix=CHARITY_PROJECT_PREFIX,
    tags=CHARITY_PROJECT_TAGS,
)
main_router.include_router(
    donation_router,
    prefix=DONATION_PREFIX,
    tags=DONATION_TAGS,
)
main_router.include_router(
    google_api_router,
    prefix=GOOGLE_PREFIX,
    tags=GOOGLE_TAGS,
)
main_router.include_router(user_router)
