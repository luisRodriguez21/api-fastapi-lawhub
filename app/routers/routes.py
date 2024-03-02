from fastapi import APIRouter
from app.routers.auth import router as auth_router

routers = APIRouter()
router_list = [auth_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)