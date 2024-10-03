import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, Query
from fastapi_gateway import route
from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from utils import verify_token
from fastapi.security import OAuth2PasswordBearer
from schemas import BuildersDapPayload

load_dotenv()

PUBLIC_SVC_BUILD_URL = os.environ.get("PUBLIC_SVC_BUILD_URL")
print(
    "<------------------ PUBLIC_SVC_BUILD_URL ",
    PUBLIC_SVC_BUILD_URL,
    " --------------------------->",
)


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()


@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_BUILD_URL,
    gateway_path="/builder/add_dap/",
    service_path="/builder/add_dap/",
    body_params=["builder_dap"],
    status_code=status.HTTP_200_OK,
    tags=["Builder-Daps"],
    dependencies=[Depends(verify_token)],
)
async def builder_add_dap(
    request: Request, response: Response, builder_dap: BuildersDapPayload
):
    """
    create builder dap
    """
    pass


@route(
    request_method=router.get,
    service_url=PUBLIC_SVC_BUILD_URL,
    gateway_path="/builder/{builder_id}/daps",
    service_path="/builder/{builder_id}/daps",
    query_params=["limit"],
    status_code=status.HTTP_200_OK,
    tags=["Builder-Daps"],
    dependencies=[Depends(verify_token)],  # Token verification dependency
)
async def get_builder_daps(
    request: Request,
    response: Response,
    builder_id: str,
    limit: int = Query(10),
):
    """
    List Builder daps
    """
    pass