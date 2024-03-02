from fastapi import APIRouter, Depends
# from dependency_injector.wiring import Provide, inject

# routes auth - login - logout - register - forgot password - reset password

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/sign-in")
# @inject
async def sign_in():
    return {"message": "Sign in completed"}