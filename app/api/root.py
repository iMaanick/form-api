from fastapi import APIRouter

from .form import form_router
from .index import index_router
root_router = APIRouter()

root_router.include_router(
    form_router,
    tags=["form"]
)

root_router.include_router(
    index_router,
)
