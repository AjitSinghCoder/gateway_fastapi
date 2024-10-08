import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends,Query,Body
from fastapi_gateway import route 
from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from utils import verify_token
from fastapi.security import OAuth2PasswordBearer
from typing import Optional,Dict
from schemas import (
    Profile,
    PrimaryDetails,
    Contact,
    Security,
    Social,
    Clubs,
    CreditCards,
    Billing,
    Login,
    ForgotPasswordRequest,
    VerifyOtpRequest,
    UpdatePasswordRequest,
    RefreshToken,
    TokenPayload,
    UsernameByIds,
)

load_dotenv()

PUBLIC_SVC_PROFILE_URL = os.environ.get("PUBLIC_SVC_PROFILE_URL")
PUBLIC_SVC_BUILD_URL = os.environ.get("PUBLIC_SVC_BUILD_URL")
print("<------------------ PUBLIC_SVC_PROFILE_URL ", PUBLIC_SVC_PROFILE_URL ," --------------------------->")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()

@route(
    request_method=router.get,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/allprofiles/",
    service_path="/allprofiles/",
    query_params=["limit"],
    status_code=status.HTTP_200_OK,
    tags=["Profiles"],
    dependencies=[Depends(verify_token)],  # Token verification dependency
)
async def all_profiles(
    request: Request,
    response: Response,
    limit: int = Query(10),
    last_evaluated_key: Optional[Dict] = Body(
        None
    ),  # Accepting last_evaluated_key as JSON input
):
    """
    List profiles
    """
    pass



@route(
    request_method=router.get,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/health",
    service_path="/health",
    status_code=status.HTTP_200_OK,
    tags=["Health"],
    dependencies=[Depends(verify_token)],
)
async def get_health(
    request: Request,
    response: Response,
):
    """
    Get health
    """
    pass

@route(
    request_method=router.get,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/get_profile/{profile_id}",
    service_path="/get_profile/{profile_id}",
    status_code=status.HTTP_200_OK,
    tags=["Profiles"],
    dependencies=[Depends(verify_token)],
)
async def get_profile(
    request: Request,
    response: Response,
    profile_id : str
):
    """
    Get profile
    """
    pass


@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/create_profile/",
    service_path="/create_profile/",
    body_params=["Profile"],
    status_code=status.HTTP_200_OK,
    tags=["Profiles"],
    dependencies=[Depends(verify_token)],
)
async def create_profile(request: Request, response: Response, Profile :Profile ):
    """
    create profile
    """
    pass


@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/update_primary_details/",
    service_path="/update_primary_details/",
    body_params=["primary_details"],
    status_code=status.HTTP_200_OK,
    tags=["Primary-Details"],
    dependencies=[Depends(verify_token)],
)
async def update_primary_details(
    request: Request, response: Response, primary_details: PrimaryDetails
):
    """
    update primary details
    """
    pass


@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/update_contact/",
    service_path="/update_contact/",
    body_params=["contact"],
    status_code=status.HTTP_200_OK,
    tags=["Primary-Details"],
    dependencies=[Depends(verify_token)],
)
async def update_contact(request: Request, response: Response, contact: Contact):
    """
    update Contact
    """
    pass


@route(
    request_method=router.put,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/update_security/",
    service_path="/update_security/",
    body_params=["security"],
    status_code=status.HTTP_200_OK,
    tags=["Primary-Details"],
    dependencies=[Depends(verify_token)],
)
async def update_security(request: Request, response: Response, security: Security):
    """
    update security
    """
    pass


@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/update_social/",
    service_path="/update_social/",
    body_params=["social"],
    tags=["Primary-Details"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)],
)
async def update_social(request: Request, response: Response, social: Social):
    """
    update Social
    """
    pass

@route(
    request_method=router.put,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/update_clubs/",
    service_path="/update_clubs/",
    body_params=["clubs"],
    status_code=status.HTTP_200_OK,
    tags=["Primary-Details"],
    dependencies=[Depends(verify_token)],
)
async def update_clubs(request: Request, response: Response, clubs: Clubs):
    """
    update clubs
    """
    pass

@route(
    request_method=router.put,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/update_billing/",
    service_path="/update_billing/",
    body_params=["billing"],
    status_code=status.HTTP_200_OK,
    tags=["Primary-Details"],
    dependencies=[Depends(verify_token)],
)
async def update_billing(
    request: Request, response: Response, billing: Billing
):
    """
    update billing
    """
    pass


@route(
    request_method=router.put,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/update_credit_cards/",
    service_path="/update_credit_cards/",
    body_params=["credit_card"],
    status_code=status.HTTP_200_OK,
    tags=["Primary-Details"],
    dependencies=[Depends(verify_token)],
)
async def update_credit_cards(
    request: Request, response: Response, credit_card: CreditCards
):
    """
    update Credit Cards
    """
    pass


@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/login/",
    service_path="/login/",
    body_params=["login"],
    tags=["Auth"],
    status_code=status.HTTP_200_OK,
)
async def login(request: Request, response: Response, login: Login):
    """
    Login
    """
    pass

@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/forgot_password/",
    service_path="/forgot_password/",
    body_params=["forgot_password"],
    tags=["Auth"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)],
)
async def forgot_password(
    request: Request, response: Response, forgot_password: ForgotPasswordRequest
):
    """
    Forget password
    """
    pass


@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/verify_otp/",
    service_path="/verify_otp/",
    body_params=["verify_otp"],
    tags=["Auth"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)],
)
async def verify_otp(
    request: Request, response: Response, verify_otp: VerifyOtpRequest
):
    """
    Verify otp
    """
    pass



@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/update_new_password/",
    service_path="/update_new_password/",
    body_params=["update_new_password"],
    tags=["Auth"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)],
)
async def update_new_password(
    request: Request, response: Response, update_new_password: UpdatePasswordRequest
):
    """
    update new password
    """
    pass



@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/refresh-token/",
    service_path="/refresh-token/",
    body_params=["refresh_token"],
    tags=["Auth"],
    status_code=status.HTTP_200_OK,
)
async def refresh_token(
    request: Request, response: Response, refresh_token: RefreshToken
):
    """
    refresh token
    """
    pass

@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/verify-token/",
    service_path="/verify-token/",
    body_params=["verify_token"],
    tags=["Google Auth"],
    status_code=status.HTTP_200_OK,
)
async def google_login(
    request: Request, response: Response, verify_token: TokenPayload
):
    """
    Login with google
    """
    pass


@route(
    request_method=router.get,
    service_url=PUBLIC_SVC_PROFILE_URL,
    gateway_path="/login-history",
    service_path="/login-history",
    status_code=status.HTTP_200_OK,
    tags=["Login-History"],
    dependencies=[Depends(verify_token)],
)
async def login_history(
    request: Request,
    response: Response,
):
    """
    Get login history
    """
    pass


@route(
    request_method=router.post,
    service_url=PUBLIC_SVC_BUILD_URL,
    gateway_path="/users/get_names_by_ids",
    service_path="/users/get_names_by_ids",
    body_params=["username_by_ids"],
    tags=["Profile"],
    status_code=status.HTTP_200_OK,
)
async def get_users_names_by_ids(
    request: Request, response: Response, username_by_ids: UsernameByIds
):
    """
    Login with google
    """
    pass
